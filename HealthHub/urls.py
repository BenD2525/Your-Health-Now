from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

app_name = 'HealthHub'

urlpatterns = [
    path('', views.home, name='home'),
    path('MyHealth/', views.health_hub, name='health_hub'),
    path('MyHealth/update', views.UpdateHealth.as_view(), name='health_hub_update'),
    path('MyHealth/history', views.health_history, name='health_hub_history'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('MyHealth/delete/<item_id>', views.delete_entry, name='health_hub_delete'),
    path('MyHealth/edit/<int:pk>', views.EditHealth.as_view(), name='health_hub_edit'),
    path('MyHealth/article/<int:pk>', views.article_detail, name='health_hub_article'),
]