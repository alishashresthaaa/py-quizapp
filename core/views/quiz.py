import random

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from core.forms import CategoryForm
from core.models import Answer
from core.models import Quiz
from core.models import QuizResponse
from core.utils import get_quiz_response

# Add login required decorator


LOGIN_URL = reverse_lazy("login")


# decorator to redirect to login page if user is not authenticated
@method_decorator(login_required(login_url=LOGIN_URL), name="dispatch")
@method_decorator(require_http_methods(["GET"]), name="dispatch")
class CategoriesView(TemplateView):
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        # add custom categoryform to context
        context = super().get_context_data(**kwargs)
        context["form"] = CategoryForm()
        return context


@method_decorator(login_required(login_url=LOGIN_URL), name="dispatch")
@method_decorator(require_http_methods(["POST"]), name="dispatch")
class StartQuizView(TemplateView):
    """View to start a quiz"""

    template_name = "quiz.html"

    def post(self, request):

        # validate category form
        category = CategoryForm(request.POST)
        if not category.is_valid():
            return HttpResponse("Invalid category", status=400)

        # get random questions from selected category
        category = category.cleaned_data["category"]
        questions = category.question_set.all()
        questions = random.sample(list(questions), min(5, len(questions)))

        # create quiz object
        quiz = Quiz.objects.create(
            user=request.user, name=f"{request.user}#{category}"
        )

        # create quiz response object
        data = {
            "id": quiz.id,
            "category": category.name,
            "questions": [],
        }
        # loop through the selected questions and answers
        for question in questions:
            question_data = {
                "text": question.question_text,
                "answers": [],
                "id": question.id,
            }
            for answer in question.answers.all():
                answer_data = {
                    "id": answer.id,
                    "text": answer.answer_text,
                }
                question_data["answers"].append(answer_data)
            data["questions"].append(question_data)
        return self.render_to_response({"quiz": data})


@method_decorator(login_required(login_url=LOGIN_URL), name="dispatch")
@method_decorator(require_http_methods(["POST"]), name="dispatch")
class QuizResultsView(TemplateView):
    """View to calculate and display quiz results"""

    template_name = "results.html"

    def post(self, request, quiz_id):
        data = self.request.POST

        # get quiz object
        try:
            quiz = Quiz.objects.get(pk=quiz_id)
        except Quiz.DoesNotExist:
            return HttpResponse("Quiz not found", status=404)

        # calculate score and save quiz response
        score = 0
        total = 0
        for question_id, answer_id in data.items():
            try:
                answer = Answer.objects.get(pk=answer_id)
            except Answer.DoesNotExist:
                return HttpResponse("Answer not found", status=404)

            is_correct = answer.is_correct
            QuizResponse.objects.create(
                question_id=question_id,
                answer_id=answer_id,
                quiz_id=quiz_id,
                is_correct=is_correct,
            )

            if is_correct:
                score += 1
            total += 1

        quiz.score = score
        quiz.save()

        percentage = (score / total) * 100
        allow_retry = percentage < 50

        result = {
            "score": score,
            "total": total,
            "quiz_id": quiz_id,
            "category": quiz.category.name,
            "percentage": percentage,
            "message": get_quiz_response(score),
            "allow_retry": allow_retry,
        }

        return self.render_to_response({"result": result})


@method_decorator(login_required(login_url=LOGIN_URL), name="dispatch")
@method_decorator(require_http_methods(["GET"]), name="dispatch")
class QuizHistoryView(TemplateView):
    template_name = "history.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # filter quizzes by user
        user = self.request.user
        quizzes = Quiz.objects.filter(user=user).order_by("-date_created")

        # calculate average, highest, and lowest scores
        average_score = sum([quiz.score for quiz in quizzes]) / len(quizzes)
        context["average_score"] = average_score
        context["highest_score"] = max([quiz.score for quiz in quizzes])
        context["lowest_score"] = min([quiz.score for quiz in quizzes])

        # append quiz data
        quizzes = {}
        for quiz in quizzes:
            quiz_data = {
                "id": quiz.id,
                "name": quiz.name,
                "score": quiz.score,
                "date_created": quiz.date_created,
                "category": quiz.category.name,
                "responses": [],
            }

            responses = QuizResponse.objects.filter(quiz=quiz)
            for response in responses:
                response_data = {
                    "question": response.question.text,
                    "answer": response.answer.text,
                    "is_correct": response.is_correct,
                }
                quiz_data["responses"].append(response_data)

            quizzes.append(quiz_data)

        context["quizzes"] = quizzes
        return context


class QuizResultView(TemplateView):
    template_name = "result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Example context data, replace with actual data retrieval logic
        context['score'] = {
            'category': 'Science'
        }
        context['result'] = {
            'percentage': 75,
            'score': 3,
            'total': 4,
            'message': 'Good job!'
        }
        return context