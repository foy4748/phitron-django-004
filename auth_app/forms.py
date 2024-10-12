from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"id": "required"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"id": "required"}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class ChangeProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        # exclude = ("password",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("password", None)
