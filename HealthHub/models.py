from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class HealthStats(models.Model):
    '''Model which allows the user to store their weight, run distance and run 
    time. Also logs user's username and date of entry.'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    run_distance = models.DecimalField(max_digits=5, decimal_places=2)
    run_time = models.DurationField()

    class Meta:
        '''Class which sorts the table in date order.'''
        db_table = 'health_stats'
        ordering = ['-date']

    def get_absolute_url(self):
        '''Allows delete view to return to health_hub_history after deletion 
        is successful.'''
        return reverse('HealthHub:health_hub_history')

    def __str__(self):
        '''Returns a string representation of this model.'''
        return f"{self.user} | {self.date}"


class Article(models.Model):
    '''Model which stores the articles for the home page. Admin is able to 
    update these using the admin panel.'''
    title = models.CharField(max_length=200, unique=True)
    topic = models.CharField(max_length=200)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()

    def __str__(self):
        '''Returns a string representation of this model.'''
        return f"{self.title}"