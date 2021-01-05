from django.shortcuts import render
from .forms import CustomUserCreationForm
# Create your views here.
def login(request):
    context = {
        'form': CustomUserCreationForm
    }
    return render(request, 'accounts/login.html', context)


def signup(request):
    pass


def logout(request):    
    pass