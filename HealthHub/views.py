from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, '')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://8000-bend2525-yourhealthnow-kfxlnwg8spb.ws-eu63.gitpod.io/HealthHub/success/')
    else:
        form = UserCreationForm()
    return render(request, 'HealthHub/signup.html', {'form': form})


def success_view(request):
    return render(request, 'HealthHub/success.html')
