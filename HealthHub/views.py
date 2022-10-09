from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .models import HealthStats, Article
from .forms import StatUpdateForm


def home(request):
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
             
        # context = {
        #     'stats': stats,
        #     'update_form': update_form,
        #     'user': stats.user,
        #     'weight': stats.weight,
        #     'date': stats.date,
        #     'run time': stats.run_time,
        #     'run distance': stats.run_distance
        # }

        if update_form.is_valid():
            obj = update_form.save(commit=False)
            obj.user = request.user
            obj.save()
            
        return redirect("HealthHub:health_hub")


class DeleteEntry(DeleteView):
    model = HealthStats
    template_name = 'health_hub_delete.html'
    success_url = reverse_lazy('HealthHub:health_hub_history')


class EditHealth(UpdateView):
    model = HealthStats
    template_name = 'health_hub_edit.html'
    fields = ['weight', 'run_distance', 'run_time']


def article_detail(request, item_id):
    article = Article.objects.get(id=item_id)
    context = {
            "title": article.title,
            "topic": article.topic,
            "featured_image": article.featured_image,
            "content": article.content,
        }   
    return render(request, 'health_hub_article.html', context)
