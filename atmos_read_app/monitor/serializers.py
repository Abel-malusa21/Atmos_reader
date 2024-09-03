from rest_framework import serializers
from .models import TempHumidityRecord

class TempHumidityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempHumidityRecord
        fields = ['id', 'temperature', 'humidity', 'timestamp']