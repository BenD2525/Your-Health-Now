from django.db import models
from django.contrib.auth.models import User


class Stats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'health_stats'
        ordering = ['-date']

    def __str__(self):
        return f"You currently weigh {self.weight}, {self.user}"