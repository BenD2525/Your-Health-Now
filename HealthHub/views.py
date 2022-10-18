from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .models import HealthStats, Article
from .forms import StatUpdateForm


def home(request):
    '''View for the home page. 
    Gathers and displays articles from Article model.'''
    serialized_articles = []
    articles = Article.objects.all()
    for article in articles:
        serialized_articles.append({
            "title": article.title,
            "topic": article.topic,
            "featured_image": article.featured_image,
            "id": article.id,
        })     
    context = {
        "articles": serialized_articles
        }
    return render(request, 'home.html', context)


def health_hub(request):
    '''View for the Health Hub page. 

    Gathers and displays latest health stats from HealthStats model.'''
    user = request.user
    if HealthStats.objects.filter(user=user):
        latest = HealthStats.objects.filter(user=request.user).latest('date')
        context = {
                    "user": latest.user,
                    "weight": latest.weight,
                    "date": latest.date,
                    "run_distance": latest.run_distance,
                    "run_time": latest.run_time,
                }
        return render(request, 'health_hub.html', context)
    else:
        context = {
                "user": user,
                "weight": " ",
                "date": "",
                "run_distance": " ",
                "run_time": " ",
            }
        return render(request, 'health_hub.html', context)


def health_history(request):
    '''View for the Health Hub History page.

    Gathers and displays all stats for current user from HealthStats model.'''
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
 

def health_hub_tracker(request):
    '''View for the Weight Tracker page. 

    Gathers and displays user's stats from HealthStats model
    and displays them using chart.js.'''
    serialized_weight = []
    serialized_date = []
    for stats in HealthStats.objects.filter(user=request.user):
        serialized_weight.append(int(
            stats.weight,
        ))
        date_only = stats.date.date()
        serialized_date.append(str(
            date_only
        ))
    serialized_weight.reverse()
    serialized_date.reverse()
    context = {
        "weight": serialized_weight,
        "date": serialized_date
        }
    return render(request, "health_hub_tracker.html", context)


class UpdateHealth(View):
    '''View for the Update Health page. 

    Uses StatUpdateForm to allow the user to update their stats.'''
    
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

        if update_form.is_valid():
            obj = update_form.save(commit=False)
            obj.user = request.user
            obj.save()
            
        return redirect("HealthHub:health_hub")


class DeleteEntry(DeleteView):
    '''View for the Delete Entry page. 

    Allows the user to confirm and action deletion of the selected entry.'''
    model = HealthStats
    template_name = 'health_hub_delete.html'
    success_url = reverse_lazy('HealthHub:health_hub_history')


class EditHealth(UpdateView):
    '''View for the Edit Stats page. 

    Allows the user to confirm and action editing of the selected entry.'''
    
    model = HealthStats
    template_name = 'health_hub_edit.html'
    fields = ['weight', 'run_distance', 'run_time']


def article_detail(request, item_id):
    '''View for the Article Detail page. 

    Displays the selected article from the Article model.'''

    article = Article.objects.get(id=item_id)
    context = {
            "title": article.title,
            "topic": article.topic,
            "featured_image": article.featured_image,
            "content": article.content,
        }   
    return render(request, 'health_hub_article.html', context)

