# core/forms.py
import re

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )


class RegisterForm(forms.Form):
    firstname = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    lastname = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    confirm_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
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
