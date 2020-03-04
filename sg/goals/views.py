from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Spending, Goal
from decimal import *
from .forms import SpendingForm, NewGoal

# Create your views here.
# View that shows the current user's goal
def currentGoal(request):
    # TODO: user needs to be authenticated
    user = request.user # change later
    goals = user.allGoals.all()
    try:
        currentGoal = goals[len(goals)-1]
    except:
        empty = True
        return render(request, 'currentGoal.html', {'empty':empty})

    form = SpendingForm()
    Context = {
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
            currentGoal.percentSpendingFromCheck = (currentGoal.totalSpending/currentGoal.checkAmount) * 100
            currentGoal.needToSpend -= currentPrice
            currentGoal.currentSpending.add(newSpend)
            currentGoal.save()

            return redirect('currentGoal')
            # TODO: redirect to the created topic page

    # TODO: do something when form is invalid
    return HttpResponse("INVALID FORM")

def spendingHistory(request):
    user = request.user
    goals = user.allGoals.all()
    empty = True
    try:
        currentGoal = goals[len(goals)-1]
    except:
        return render(request, 'spendingHistory.html', {'empty':empty})
    
    currentSpending = currentGoal.currentSpending.all()

    if len(currentSpending) != 0:
        empty = False

    context = {
        'currentGoal': currentGoal,
        'currentSpending': currentSpending,
        'empty': empty,
    }
    print(currentSpending)
    return render(request, 'spendingHistory.html', context)

def newGoal(request):
    form = NewGoal()
    user = request.user
    allGoal = user.allGoals.all()
    print(len(allGoal))

    context = {
        'form':form,
    }
    return render(request, 'newGoal.html', context)

def addGoal(request):
    if request.method == 'POST':
        form = NewGoal(request.POST)
        user = request.user
        if form.is_valid():
            percentGoal = form.cleaned_data.get('percentGoal')
            checkAmount = form.cleaned_data.get('checkAmount')
            ntsDuration = form.cleaned_data.get('ntsDuration')
            needToSpend = checkAmount * (percentGoal/100)
            addedGoal = Goal.objects.create(
                spender=user,
                needToSpend=needToSpend,
                checkAmount=checkAmount,
                percentGoal=percentGoal,
                ntsDuration=ntsDuration
            )
            return redirect('currentGoal')

    # TODO: do something when form is invalid
    return HttpResponse("INVALID FORM")

def goalHistory(request):
    user = request.user
    allGoal = user.allGoals.all()

    empty = True
    try:
        excludeGoal = allGoal[len(allGoal)-1].id
    except:
        return render(request, 'goalHistory.html', {'empty':empty})

    goals = user.allGoals.exclude(id=excludeGoal).all()

    if len(goals) != 0:
        empty = False

    spendingList = []
    for currentGoal in goals:
        spendingList.append(list(currentGoal.currentSpending.all()))
    context = {
        'goals':goals,
        'spendingList': spendingList,
        'empty': empty
    }

    for i in spendingList:
        print(i)
        if i is None:
            print("NONE")

    return render(request, 'goalHistory.html', context)
