from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Spending, Goal
from decimal import *

# Create your views here.
# View that shows the current user's goal
def currentGoal(request):
    # if !request.user.is_authenticated():
    #     redirect to login
    user = User.objects.first() # change later
    goals = user.allGoals.all()
    currentGoal = goals[len(goals)-1]

    context = {
        'currentGoal': currentGoal
    }
    return render(request, 'currentGoal.html', context)