from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

app_name = 'HealthHub'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('success/', views.success_view, name='success'),
]