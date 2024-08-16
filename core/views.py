import random

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.urls import path
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from core.forms import CategoryForm
from core.forms import LoginForm
from core.forms import RegisterForm
from core.models import Answer
from core.models import Category
from core.models import Quiz
from core.models import QuizResponse
from core.utils import get_quiz_response


class LoginView(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginForm()
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("categories"))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("categories"))
            else:
                form.add_error(None, "Invalid username or password")
        return self.render_to_response({"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class RegisterView(TemplateView):
    template_name = "register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RegisterForm()
        return context

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            get_user_model().objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
                first_name=form.cleaned_data["firstname"],
                last_name=form.cleaned_data["lastname"],
            )
            return redirect(reverse("login"))
        return self.render_to_response({"form": form})


@method_decorator(
    login_required(login_url=reverse_lazy("login")), name="dispatch"
)
@method_decorator(require_http_methods(["GET"]), name="dispatch")
class CategoriesView(TemplateView):
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CategoryForm()
        return context


@method_decorator(
    login_required(login_url=reverse_lazy("login")), name="dispatch"
)
@method_decorator(require_http_methods(["POST"]), name="dispatch")
class StartQuizView(TemplateView):
    template_name = "quiz.html"

    def post(self, request):

        category = CategoryForm(request.POST)
        if not category.is_valid():
            return HttpResponse("Invalid category", status=400)

        category = category.cleaned_data["category"]
        questions = category.question_set.all()
        questions = random.sample(list(questions), min(5, len(questions)))

        quiz = Quiz.objects.create(
            user=request.user, name=f"{request.user}#{category}"
        )
        data = {
            "id": quiz.id,
            "category": category.name,
            "questions": [],
        }
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


@method_decorator(
    login_required(login_url=reverse_lazy("login")), name="dispatch"
)
@method_decorator(require_http_methods(["POST"]), name="dispatch")
class QuizResultsView(TemplateView):
    template_name = "results.html"

    def post(self, request, quiz_id):
        data = self.request.POST
        try:
            quiz = Quiz.objects.get(pk=quiz_id)
        except Quiz.DoesNotExist:
            return HttpResponse("Quiz not found", status=404)

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


@method_decorator(
    login_required(login_url=reverse_lazy("login")), name="dispatch"
)
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