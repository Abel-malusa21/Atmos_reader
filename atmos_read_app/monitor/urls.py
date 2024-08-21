from django.urls import path, include
from rest_framework import routers
from .views import TempHumidityRecordViewSet

router = routers.DefaultRouter()
router.register(r'records', TempHumidityRecordViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
