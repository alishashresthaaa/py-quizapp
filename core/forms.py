from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True, placeholder="First Name" )
    last_name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)


