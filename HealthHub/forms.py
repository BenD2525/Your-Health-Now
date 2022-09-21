from django import forms
from .models import HealthStats
from django.forms import ModelForm


class StatUpdateForm(forms.ModelForm):
    class Meta:
        model = HealthStats
        fields = ('weight', 'run_distance', 'run_time')
        labels = {'weight': 'Weight (lbs)', 'run_distance': 'Run distance (km)', 'run_time': 'Run time (HH:MM:SS)'}
    
