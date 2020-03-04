from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Create your views here.
urlpatterns = [
    path("signup", views.signup, name='signup'),
    path("logout", auth_views.LogoutView.as_view(), name='logout'),
    path("test", views.test, name='test')
]