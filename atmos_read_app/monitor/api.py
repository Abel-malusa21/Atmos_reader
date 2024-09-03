# api.py
from rest_framework import generics, serializers
from .models import TempHumidityRecord

class TempHumidityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempHumidityRecord
        fields = ['id', 'temperature', 'humidity', 'timestamp']

class TempHumidityRecordListCreate(generics.ListCreateAPIView):
    queryset = TempHumidityRecord.objects.all().order_by('-timestamp')
    serializer_class = TempHumidityRecordSerializer

class TempHumidityRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TempHumidityRecord.objects.all()
    serializer_class = TempHumidityRecordSerializer
