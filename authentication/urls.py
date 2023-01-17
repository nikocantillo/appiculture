"""Users URLs."""

# Django
from django.urls import path

# View
from . import views

from django.contrib.auth import views as auth_views #import this

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),

    # Management
    # path(
    #     route='login/',
    #     view=views.LoginView.as_view(),
    #     name='login'
    # ),
    # path(
    #     route='logout/',
    #     view=views.LogoutView.as_view(),
    #     name='logout'
    # ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    # path(
    #     route='me/profile/',
    #     view=views.UpdateProfileView.as_view(),
    #     name='update'
    # ),

    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    path("password_reset", views.password_reset_request, name="password_reset")

]