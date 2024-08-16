from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("categories/", views.CategoriesView.as_view(), name="categories"),
    path(
        "start/",
        views.StartQuizView.as_view(),
        name="start_quiz",
    ),
    path(
        "submit/<int:quiz_id>/",
        views.QuizResultsView.as_view(),
        name="quiz_results",
    ),
    path("history/", views.QuizHistoryView.as_view(), name="quiz_history"),
]
