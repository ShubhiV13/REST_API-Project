from django.urls import path
from .views import (
    register_api, CustomAuthToken, login_page, register_page, dashboard_page
)

urlpatterns = [
    path('', login_page, name='login'),           # First page = Login
    path('register/', register_page, name='register'),
    path('dashboard/', dashboard_page, name='dashboard'),

    # API
    path('api/register/', register_api, name='api-register'),
    path('api/login/', CustomAuthToken.as_view(), name='api-login'),
]