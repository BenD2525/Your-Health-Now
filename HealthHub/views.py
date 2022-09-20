from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from .models import HealthStats
from .forms import StatUpdateForm


def home(request):
    return render(request, 'home.html')


def health_hub(request):
    latest = HealthStats.objects.filter(user=request.user).latest('date')
    context = {
            "user": latest.user,
            "weight": latest.weight,
            "date": latest.date,
            "run_distance": latest.run_distance,
            "run_time": latest.run_time,
        }
    return render(request, 'health_hub.html', context)


def health_history(request):
    serialized_stats = []
    for stats in HealthStats.objects.filter(user=request.user):
        serialized_stats.append({
            "user": stats.user,
            "weight": stats.weight,
            "date": stats.date,
            "run_distance": stats.run_distance,
            "run_time": stats.run_time,
            "id": stats.id,
        })
    context = {
        "stats": serialized_stats
        }
    return render(request, 'health_hub_history.html', context)
 

class UpdateHealth(View):
    
    def get(self, request, *args, **kwargs):

        stats = HealthStats
        update_form = StatUpdateForm
             
        context = {
            'stats': stats,
            'update_form': update_form,
            'user': stats.user,
            'weight': stats.weight,
            'date': stats.date,
        }
        return render(request, 'health_hub_update.html', context)
    
    def post(self, request, *args, **kwargs):

        stats = HealthStats
        update_form = StatUpdateForm(data=request.POST)
             
        context = {
            'stats': stats,
            'update_form': update_form,
            'user': stats.user,
            'weight': stats.weight,
            'date': stats.date,
            'run time': stats.run_time,
            'run distance': stats.run_distance
        }

        if update_form.is_valid():
            update_form.save()
            
        return render(request, 'health_hub_update.html', context)


def delete_entry(request, item_id):
    entry = get_object_or_404(HealthStats, id=item_id)
    entry.delete()
    return redirect("HealthHub:health_hub_history")
