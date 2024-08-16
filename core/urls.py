from django.urls import path

from core.views import auth
from core.views import profile
from core.views import quiz

urlpatterns = [
    # auth views
    path("", quiz.CategoriesView.as_view(), name="categories"),
    path("login/", auth.LoginView.as_view(), name="login"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    path("register/", auth.RegisterView.as_view(), name="register"),
    # quiz views
    path("start/", quiz.StartQuizView.as_view(), name="start_quiz"),
    path(
        "submit/<int:quiz_id>/",
        quiz.QuizResultsView.as_view(),
        name="quiz_results",
    ),
    path("scores/", quiz.QuizHistoryView.as_view(), name="scores"),
    path("profile/", profile.ProfileView.as_view(), name="profile"),
    path(
        "edit-profile/", profile.EditProfileView.as_view(), name="edit_profile"
    ),
]
