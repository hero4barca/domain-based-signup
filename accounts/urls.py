from django.urls import path, include

from django.contrib.auth import views as auth_views

from .views import register, CustomLoginView, home

urlpatterns = [
    path('', CustomLoginView.as_view(), name='root' ),
    path('login/', CustomLoginView.as_view() , name='login'),
    path('logout/', auth_views.LogoutView.as_view() , name='logout'),

    path('register/', register, name='signup'),

    path('profile/', home, name='profile' ),
]