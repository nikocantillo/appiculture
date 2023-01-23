"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from .models import User as Profile
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.http import urlsafe_base64_decode

UserModel = get_user_model()

class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


# class ChangePasswordForm(forms.Form):
#     """
#     A form that lets a user change set their password without entering the old
#     password
#     """
#     # def __init__(self, request, *args, **kwargs):
#     #     self.user = request
#     #     super().__init__(*args, **kwargs)

    
#     error_messages = {
#         "password_mismatch": _("The two password fields didn’t match."),
#     }
#     new_password1 = forms.CharField(
#         label=_("New password"),
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#         strip=False,
#         help_text=password_validation.password_validators_help_text_html(),
#     )
#     new_password2 = forms.CharField(
#         label=_("New password confirmation"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#     )

#     class Meta:
#         model=Profile
#         fields=('new_password1','new_password2')

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = self.user
#         return kwargs

    
#     def clean_new_password2(self):

#         cleaned_data = super(ChangePasswordForm, self).clean()
#         password1 = cleaned_data.get("new_password1")
#         password2 = cleaned_data.get("new_password2")
#         if password1 and password2:
#             if password1 != password2:
#                 raise ValidationError(
#                     self.error_messages["password_mismatch"],
#                     code="password_mismatch",
#                 )
#         password_validation.validate_password(password2)
#         return cleaned_data

#     def save(self, commit=True):
#         password = self.cleaned_data["new_password1"]
#         self.user.set_password(password)
#         if commit:
#             self.user.save()
#         return self.user
