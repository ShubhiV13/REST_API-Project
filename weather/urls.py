from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeatherViewSet, home, login_view, logout_view, health_check

router = DefaultRouter()
router.register('weather', WeatherViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API endpoint: /api/weather/
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('health/', health_check, name='health'), 
]