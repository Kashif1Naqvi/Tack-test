from .models import Performance, DailyPerformance
from django.http import JsonResponse
from datetime import date
import random


def daily_performance(request):
    performance = Performance.objects.get(id=1) # imagin id is 1

    min_roi_total = int(performance.revenue) / int(performance.cost) * 100
    
    min_roi = DailyPerformance.objects.model.filter_by_min_roi(min_roi=float(min_roi_total))
    
    return JsonResponse({
        "message": min_roi
    })

def filter_by_min_roi(request):
    length = 1
    daily_revenue_value = 0
    performances = Performance.objects.all()
    for performance in performances:
        roi_total = int(performance.revenue) / int(performance.cost) * 100
        if(roi_total > 50):
            length *= 2
        random_number = random.uniform(0.5, 2)

        if(performance.creation_date == date.today()):
            daily_revenue = int(performance.revenue) * random_number
            daily_revenue_value = daily_revenue

    return JsonResponse({
        "Total Length": length,
        "daily_revenue_value": daily_revenue_value
    })

