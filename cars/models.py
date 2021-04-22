from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class CarModel(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    carmodel = models.ForeignKey(CarModel,on_delete=models.CASCADE)

    COLOR_UNKNOWN = 0
    WHITE = 1
    BLACK = 2
    RED = 3
    YELLOW = 4

    COLOR_CHOICES = [
        (COLOR_UNKNOWN, 'Unkown'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
        (RED, 'Red'),
        (YELLOW, 'Yellow')
    ]

    color = models.IntegerField(choices=COLOR_CHOICES, default=COLOR_UNKNOWN, null=False)

    def get_color(self):
        return  self.get_color_display()
