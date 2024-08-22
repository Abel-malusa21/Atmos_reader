from rest_framework import serializers
from .models import TempHumidityRecord
from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer

class TempHumidityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempHumidityRecord
        fields = ['id', 'temperature', 'humidity', 'timestamp']
        
class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
