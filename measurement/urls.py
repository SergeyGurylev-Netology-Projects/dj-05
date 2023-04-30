from django.urls import path
from measurement.views import SensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
