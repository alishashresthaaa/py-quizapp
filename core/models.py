from django.contrib.auth import get_user_model
from django.db import models


class BaseModel(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.__class__.__name__} #{self.pk}"

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pk}#{self.name}"


class Question(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Answer(BaseModel):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Quiz(BaseModel):
    """Represents a quiz that a user has taken"""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class QuizResponse(BaseModel):
    """Stores the user's response to a quiz question"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.question.question_text + " - " + self.answer.answer_text
