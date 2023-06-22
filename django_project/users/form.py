from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from .models import User



# class RegisterStaffForm(UserCreationForm):
#     password1 = forms.CharField(
#         label='Password',
#         widget=forms.PasswordInput,
#         validators=[validate_password]
#     )

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class RegisterStaffForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text="Your password must contain at least 8 characters.",
        error_messages={
            'required': "Please enter your password.",
            'min_length': "Your password must be at least 8 characters long.",
        }
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        error_messages={
            'required': "Please confirm your password.",
            'min_length': "Your password must be at least 8 characters long.",
            'mismatch': "The two passwords do not match.",
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

