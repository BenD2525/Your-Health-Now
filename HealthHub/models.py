from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class HealthStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    run_distance = models.DecimalField(max_digits=5, decimal_places=2)
    run_time = models.DurationField()

    class Meta:
        db_table = 'health_stats'
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('HealthHub:health_hub_history')

    def __str__(self):
        return f"{self.user} | {self.date}"