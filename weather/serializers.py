from rest_framework import serializers
from .models import Weather
import random

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'city', 'date', 'temperature', 'humidity', 'condition']
        read_only_fields = ['temperature', 'humidity', 'condition']

    def create(self, validated_data):
        # Generate random weather data
        validated_data['temperature'] = round(random.uniform(25, 40), 1)
        validated_data['humidity'] = random.randint(40, 90)
        validated_data['condition'] = random.choice(
            ["Sunny", "Cloudy", "Rainy", "Windy"]
        )
        
        # Check if weather for this city and date already exists
        existing = Weather.objects.filter(
            city=validated_data['city'],
            date=validated_data['date']
        ).first()
        
        if existing:
            # Update existing record
            existing.temperature = validated_data['temperature']
            existing.humidity = validated_data['humidity']
            existing.condition = validated_data['condition']
            existing.save()
            return existing
        
        return Weather.objects.create(**validated_data)