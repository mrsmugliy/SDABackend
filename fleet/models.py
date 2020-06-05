from django.db import models
models


PETROL_CHOISES = (
    (1, 'LPG'),
    (2, 'DIESEL'),
    (3, 'ELECTRIC'),
    (4, 'HYBRID'),
)

# Create your models here.
class Car(models.Model):

    brand = models.CharField(max_length=12, default="Brand")
    petrol = models.IntegerField(choices=PETROL_CHOISES, default=1)
    model = models.CharField(max_length=32)
    year = models.IntegerField()

    def __str__(self):
        return "%s %s (%i)" % (self.brand, self.model, self.year)


class Truck(Car):

    load = models.IntegerField()