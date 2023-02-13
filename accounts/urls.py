from django.urls import path, include

from django.contrib.auth import views as auth_views
from .views import register, CustomLoginView, home

urlpatterns = [
    path('login/', CustomLoginView.as_view() , name='login'),
    path('register/', register, name='signup'),
    path('profile/', home, name='profile' ),
]