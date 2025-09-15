# Ex02 Django ORM Web Application
## Date: 15/09/2025

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
#admin.py

from django.contrib import admin
from .models import Car   # Make sure your model is named Car in models.py

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'brand', 'model', 'price', 'year')

admin.site.register(Car, CarAdmin)

#models.py

from django.db import models

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

```

## OUTPUT

![alt text](<Screenshot 2025-09-15 102313.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
