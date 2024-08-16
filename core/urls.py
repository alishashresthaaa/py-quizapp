from django.urls import path

from core.views import auth
from core.views import quiz

urlpatterns = [
    # auth views
    path("login/", auth.LoginView.as_view(), name="login"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    path("register/", auth.RegisterView.as_view(), name="register"),
    # quiz views
    path("categories/", quiz.CategoriesView.as_view(), name="categories"),
    path("start/", quiz.StartQuizView.as_view(), name="start_quiz"),
    path(
        "submit/<int:quiz_id>/",
        quiz.QuizResultsView.as_view(),
        name="quiz_results",
    ),
    path("history/", quiz.QuizHistoryView.as_view(), name="quiz_history"),
    path("result/", quiz.QuizResultView.as_view(), name="result"),
    path("scores/", quiz.QuizScoresView.as_view(), name="quiz_scores"),
]
