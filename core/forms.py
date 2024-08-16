# core/forms.py
import re

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )


class RegisterForm(forms.Form):
    firstname = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your First Name'})
    )
    lastname = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your Last Name'})
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your Username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email'})
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your Password'})
    )
    confirm_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your Confirm Password'})
    )

    def clean_firstname(self):
        firstname = self.cleaned_data.get('firstname')
        if not firstname.isalpha():
            raise forms.ValidationError("First name must contain only letters.")
        return firstname

    def clean_lastname(self):
        lastname = self.cleaned_data.get('lastname')
        if not lastname.isalpha():
            raise forms.ValidationError("Last name must contain only letters.")
        return lastname

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.search(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
            raise forms.ValidationError("Password must be combination of letters and numbers.")
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password


CATEGORY_CHOICES = [
    ('science', 'Science'),
    ('math', 'Math'),
    ('history', 'History'),
    ('literature', 'Literature'),
]


class CategoryForm(forms.Form):
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'placeholder': 'Select Category'})
    )
