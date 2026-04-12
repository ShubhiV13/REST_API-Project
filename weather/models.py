from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.IntegerField()
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.city