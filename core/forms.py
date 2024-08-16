# core/forms.py
import re

from django import forms
from django.contrib.auth.models import User

from core.models import Category


class LoginForm(forms.Form):
    """Form for user login"""

    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Enter your username"}),
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter your password"}
        ),
    )


class RegisterForm(forms.Form):
    """Form for registering a new user"""

    firstname = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Enter your First Name"}),
    )
    lastname = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Enter your Last Name"}),
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Enter your Username"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter your Email"})
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter your Password"}
        ),
    )
    confirm_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter your Confirm Password"}
        ),
    )

    def clean_firstname(self):
        firstname = self.cleaned_data.get("firstname")
        if not firstname.isalpha():
            raise forms.ValidationError(
                "First name must contain only letters."
            )
        return firstname

    def clean_lastname(self):
        lastname = self.cleaned_data.get("lastname")
        if not lastname.isalpha():
            raise forms.ValidationError("Last name must contain only letters.")
        return lastname

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not re.search(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
            raise forms.ValidationError(
                "Password must be combination of letters and numbers and at least 8 characters."
            )
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password


class CategoryForm(forms.Form):
    """Form for selecting a category"""

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"placeholder": "Select Category"}),
        empty_label=None,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial value to the first object in the queryset
        first_question = self.fields["category"].queryset.first()
        if first_question:
            self.fields["category"].initial = first_question


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("First name cannot be empty.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("Last name cannot be empty.")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email cannot be empty.")
        return email
