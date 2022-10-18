from django import forms
from .models import HealthStats


class StatUpdateForm(forms.ModelForm):
    '''Form which allows the user to update their stats for the HealthStats 
    model.'''
    class Meta:
        '''Class which specifies setup of the form.'''
        model = HealthStats
        fields = ('weight', 'run_distance', 'run_time')
        labels = {'weight': 'Weight (lbs)', 'run_distance': 'Run distance (km)', 'run_time': 'Run time (HH:MM:SS)'}
    
