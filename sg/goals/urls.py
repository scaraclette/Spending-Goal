from django.urls import path
from . import views

'''
URL notes:
1. TODO: when user  is not authenticated, redirect to login page
'''

urlpatterns = [
    path("", views.currentGoal, name='currentGoal'),
    path("add-spending", views.addSpending, name='addSpending')
]