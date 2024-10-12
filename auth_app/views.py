from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView

from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.views.generic.edit import UpdateView

from auth_app.forms import ChangeProfileForm, RegisterForm


# Create your views here.
class ShowRegistrationForm(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "auth_app/registration_form.html"

    def get_success_url(self):
        # next_url = self.request.GET.get("next", reverse_lazy("order_car:my_orders"))
        next_url = self.request.GET.get("next", "/")
        return next_url

    def form_valid(self, form):
        valid = super(ShowRegistrationForm, self).form_valid(form)
        username, password = form.cleaned_data.get("username"), form.cleaned_data.get(
            "password1"
        )
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        messages.success(self.request, "Registered and Logged in successfully")
        return valid


class ShowLoginForm(LoginView):
    form_class = AuthenticationForm
    template_name = "auth_app/login_form.html"

    def get_success_url(self):
        # next_url = self.request.GET.get("next", reverse_lazy("order_car:my_orders"))
        next_url = self.request.GET.get("next", "/")
        return next_url

    def form_valid(self, form):
        messages.success(self.request, "Logged in successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "FAILED to Login")
        return super().form_invalid(form)


class LogoutUser(LoginRequiredMixin, View):
    def get(self, req):
        logout(req)
        messages.success(req, "Logged Out")
        return redirect("/")


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    # success_url = reverse_lazy("order_car:my_orders")
    success_url = "/"
    template_name = "auth_app/change_password.html"

    def form_valid(self, form):
        messages.success(self.request, "Changed password successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "FAILED to Change password")
        return super().form_invalid(form)


class ChangeProfileView(LoginRequiredMixin, UpdateView):
    form_class = ChangeProfileForm
    # success_url = reverse_lazy("order_car:my_orders")
    success_url = "/"
    template_name = "auth_app/change_profile.html"

    def get_object(self, queryset=None):
        # This method is used to get the instance of the object to be updated
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Updated profile successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "FAILED to Update Profile")
        return super().form_invalid(form)
