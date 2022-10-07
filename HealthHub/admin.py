from django.contrib import admin
from .models import HealthStats, Article

# Register your models here.
admin.site.register(HealthStats)
admin.site.register(Article)
