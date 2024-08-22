from django.contrib import admin
from django.urls import path, include
from monitor.views import index
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecordViewSet

router = DefaultRouter()
router.register(r'records', RecordViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('monitor.urls')),  # Include API URLs from monitor app
    path('', index, name='index'),  # Map the root URL to the index view
]
