from django.db import models

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
