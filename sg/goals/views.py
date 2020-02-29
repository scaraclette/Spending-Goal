from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Spending, Goal
from decimal import *
from .forms import SpendingForm

# Create your views here.
# View that shows the current user's goal
def currentGoal(request):
    # if !request.user.is_authenticated():
    #     redirect to login
    user = User.objects.first() # change later
    goals = user.allGoals.all()
    currentGoal = goals[len(goals)-1]
    form = SpendingForm()
    context = {
        'currentGoal': currentGoal,
        'form': form,
    }
    return render(request, 'currentGoal.html', context)

def addSpending(request):
    if request.method == 'POST':
        form = SpendingForm(request.POST)
        user = request.user
        goals = user.allGoals.all()
        currentGoal = goals[len(goals)-1]
        if form.is_valid():
            currentPrice=form.cleaned_data.get('price')
            # Create new form object
            newSpend = Spending.objects.create(
                price=currentPrice,
                item=form.cleaned_data.get('item')
            )
            # Add totalSpending
            currentGoal.totalSpending += currentPrice
            currentGoal.needToSpend -= currentPrice
            currentGoal.currentSpending.add(newSpend)
            currentGoal.save()

            return redirect('currentGoal')
            # TODO: redirect to the created topic page

    return HttpResponse("GET REQUEST")