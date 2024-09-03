# urls.py in monitor
from django.urls import path
from .api import TempHumidityRecordListCreate, TempHumidityRecordDetail

urlpatterns = [
    path('records/', TempHumidityRecordListCreate.as_view(), name='record-list-create'),
    path('records/<int:pk>/', TempHumidityRecordDetail.as_view(), name='record-detail'),
]
