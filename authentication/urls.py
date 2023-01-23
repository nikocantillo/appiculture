"""Users URLs."""

# Django
from django.urls import path, reverse_lazy

# View
from . import views

from django.contrib.auth import views as auth_views #import this

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<token>/', views.change_password, name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<token>/', views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('home:password_reset_complete'),template_name="authentication/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/complete/', views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'), name='password_reset_complete'),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
]