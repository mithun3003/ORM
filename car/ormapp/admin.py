from django.contrib import admin
from .models import Car   # Make sure your model is named Car in models.py

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'brand', 'model', 'price', 'year')

admin.site.register(Car, CarAdmin)
