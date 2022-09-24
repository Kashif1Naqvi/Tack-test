from django.test import TestCase
from app.models import Performance, DailyPerformance
from datetime import date
import random
# Create your tests here.


class BackendTest(TestCase):
    def setUp(self):
        Performance.objects.create(cost=10, revenue=20, creation_date=date.today())
        Performance.objects.create(cost=14, revenue=30, creation_date=date.today())

    def daily_performance(self):
        performance = Performance.objects.get(cost=10, revenue=20) # imagin id is 1
        min_roi_total = int(performance.revenue) / int(performance.cost) * 100
        min_roi = DailyPerformance.objects.model.filter_by_min_roi(min_roi=float(min_roi_total))
        self.assertEqual(min_roi, "200.0%")

    
    def filter_by_min_roi(self):
        length = 1
        daily_revenue_value = 0
        performances = Performance.objects.all()
        for performance in performances:
            roi_total = int(performance.revenue) / int(performance.cost) * 100
            if(roi_total > 50):
                length *= 2
                
            if(performance.creation_date == date.today()):
                daily_revenue = int(performance.revenue) *  0.9 #replace with some specific number for testing
                daily_revenue_value = daily_revenue
        
        self.assertEqual(length, 4)
        self.assertEqual(daily_revenue_value, 27.0)
     