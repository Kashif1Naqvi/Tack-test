from django.db import models

# Create your models here.


class Performance(models.Model):
    cost = models.CharField(max_length=100)
    revenue = models.CharField(max_length=100)
    creation_date = models.DateField(auto_now=False, auto_now_add=False)
    

class HourlyPerformance(Performance):
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)


class DailyPerformance(Performance):
    
    date = models.DateField(auto_now=False, auto_now_add=False)

    def filter_by_min_roi(min_roi: float):
        return f"{min_roi}%"

