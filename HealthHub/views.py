from django.shortcuts import render
from .models import Stats
from .forms import StatUpdateForm
from django.views import generic, View
from django.shortcuts import get_object_or_404
# from django.contrib.auth import authenticate


def home(request):
    return render(request, 'home.html')


def health_hub(request):
    return render(request, 'health_hub.html')

def HealthHistory(request):
    return render(request, 'health_hub_history.html')


class UpdateHealth(View):
    
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
        return render(request, 'health_hub_update.html', context)
    
    def post(self, request, *args, **kwargs):

        stats = Stats
        update_form = StatUpdateForm(data=request.POST)
             
        context = {
            'stats': stats,
            "update_form": update_form,
            'user': stats.user,
            'weight': stats.weight,
            'date': stats.date,
            'run time': stats.run_time,
            'run distance': stats.run_distance
        }
        return render(request, 'health_hub_update.html', context)
