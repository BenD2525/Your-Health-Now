from django.shortcuts import render, redirect
from .forms import RegistrationForm


def home(request):
    return render(request, 'HealthHub/home.html')


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://8000-bend2525-yourhealthnow-kfxlnwg8spb.ws-eu63.gitpod.io/success/')
    else:
        form = RegistrationForm()
    return render(request, 'HealthHub/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://8000-bend2525-yourhealthnow-kfxlnwg8spb.ws-eu63.gitpod.io/')
    else:
        form = RegistrationForm()
    return render(request, 'HealthHub/login.html', {'form': form})


def success_view(request):
    return render(request, 'HealthHub/success.html')
