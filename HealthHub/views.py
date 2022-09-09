from django.shortcuts import render
from .models import Stats
from .forms import StatUpdateForm
from django.views import generic, View
from django.shortcuts import get_object_or_404
# from django.contrib.auth import authenticate
# from django.core.exceptions import ValidationError
# from .forms import RegistrationForm, LoginForm


def home(request):
    return render(request, 'home.html')


class MyHealth(View):
    
    def get(self, request, *args, **kwargs):

        stats = Stats
        update_form = StatUpdateForm
             
        context = {
            'stats': stats,
            "update_form": update_form,
            'user': stats.user,
            'weight': stats.weight,
            'date': stats.date,
        }
        return render(request, 'MyHealth.html', context)


# def signup(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('https://8000-bend2525-yourhealthnow-kfxlnwg8spb.ws-eu63.gitpod.io/success/')
#     else:
#         form = RegistrationForm()
#     return render(request, 'HealthHub/signup.html', {'form': form})


# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = LoginForm.username
#             password = LoginForm.password
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 form.save()
#                 home(request)
#             else:
#                 return ValidationError("Your username or password are incorrect. Try again.")
#     else:
#         form = LoginForm()
#     return render(request, 'HealthHub/login.html', {'form': form})


# def logout(request):
#     return render(request, 'HealthHub/logout.html')


# def success_view(request):
#     return render(request, 'HealthHub/success.html')
