from django.db import models
from django.contrib.auth.models import User


class HealthStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    run_distance = models.IntegerField(default=5)
    run_time = models.TimeField()

    class Meta:
        db_table = 'health_stats'
        ordering = ['-date']

    def __str__(self):
        return f"{self.user}|{self.date}"