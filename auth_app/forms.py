from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

from auth_app.models import Profile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"id": "required"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"id": "required"}))

    # Profile related fields
    # Doesn't need it yet

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def save(self, commit=True):
        current_user = super().save(commit=False)
        if commit is True:
            current_user.save()  # Saving User in DB
            Profile.objects.create(user=current_user)

        return current_user


class ChangeProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        # exclude = ("password",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("password", None)


class DepositeForm(forms.Form):
    deposite_amount = forms.DecimalField(max_digits=12, min_value=0.00)

    class Meta:
        model = Profile
