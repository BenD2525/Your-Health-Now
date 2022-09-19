from django.shortcuts import render
from django.views import View, generic
# from django.contrib.auth.models import User
from .models import HealthStats
from .forms import StatUpdateForm


def home(request):
    return render(request, 'home.html')


def health_hub(request):
    model = HealthStats
    
    def get_queryset(self):
        user = self.user
        latest = HealthStats.objects.filter(user=user).latest('date')
        return latest

    context = {
            "user": model.user,
            "weight": model.weight,
            "date": model.date,
            "run_distance": model.run_distance,
            "run_time": model.run_time,
            "stats": HealthStats,
            "latest": get_queryset(model)
        }
    return render(request, 'health_hub.html', context)


class HealthHistory(generic.TemplateView):
    model = HealthStats
    template_name = 'health_hub_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # user = User()
        context['stats'] = HealthStats.objects.all()
        return context
    # queryset = HealthStats.objects.all()
    # context = {
    #         "user": model.user,
    #         "weight": model.weight,
    #         "date": model.date,
    #         "run_distance": model.run_distance,
    #         "run_time": model.run_time,
    #         "stats": HealthStats
    #     }
   

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
