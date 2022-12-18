from django.contrib import admin
from django.urls import path, include
from authentication.views import home,signin,signout,signup

urlpatterns = [
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
]
