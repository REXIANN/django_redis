from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    
    context = { 'form': form }
    return render(request, 'accounts/form.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    
    context = { 'form': form }
    return render(request, 'accounts/form.html', context)


@login_required
def logout(request):    
    user_logout(request)
    return redirect('/')