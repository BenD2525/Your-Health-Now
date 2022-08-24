from django.shortcuts import render

def signup(request):
    return render(request, 'HealthHub/signup.html')
