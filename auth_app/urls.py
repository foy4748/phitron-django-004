from django.urls import path
from . import views


app_name = "auth"

urlpatterns = [
    # For Django Hard Reload
    path("register/", views.ShowRegistrationForm.as_view(), name="registration_form"),
    path("", views.ShowLoginForm.as_view(), name="login_form"),
    path("logout/", views.LogoutUser.as_view(), name="logout"),
    path(
        "password-change/", views.ChangePasswordView.as_view(), name="change_password"
    ),
    path("profile-change/", views.ChangeProfileView.as_view(), name="change_profile"),
    path(
        "deposite-balance/", views.DepositeBalanceView.as_view(), name="deposite_form"
    ),
]
