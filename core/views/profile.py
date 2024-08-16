from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

from core import forms
from core.forms import EditProfileForm

LOGIN_URL = reverse_lazy("login")


@method_decorator(login_required(login_url=LOGIN_URL), name="dispatch")
@method_decorator(require_http_methods(["GET"]), name="dispatch")
class ProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        return context


@method_decorator(login_required(login_url=LOGIN_URL), name="dispatch")
@method_decorator(require_http_methods(["GET", "POST"]), name="dispatch")
class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = "edit_profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user
