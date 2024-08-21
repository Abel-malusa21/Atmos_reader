from django.db import models

class TempHumidityRecord(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Temp: {self.temperature}, Humidity: {self.humidity} at {self.timestamp}"
