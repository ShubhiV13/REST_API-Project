from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Weather
from .serializers import WeatherSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session.set_expiry(3600)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# Health check for Render
@api_view(['GET'])
def health_check(request):
    return Response({'status': 'healthy'}, status=200)