from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import HomeView


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    # path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('courses/', include(('courses.urls'), namespace='courses')),

]