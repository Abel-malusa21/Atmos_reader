from rest_framework import viewsets
from .models import TempHumidityRecord
from .serializers import TempHumidityRecordSerializer
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

class TempHumidityRecordViewSet(viewsets.ModelViewSet):
    queryset = TempHumidityRecord.objects.all().order_by('-timestamp')
    serializer_class = TempHumidityRecordSerializer
