from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('newGoal')

    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def test(request):
    return HttpResponse("logged out")