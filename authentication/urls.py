"""Users URLs."""

# Django
from django.urls import path

# View
from . import views


urlpatterns = [
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),

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
    )

]