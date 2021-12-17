from django.db import models
from .shop import Shop
from django.core.validators import RegexValidator

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class CarModel(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def get_carmodel_choices(cls):
        models = CarModel.objects.all()
        choices = list()
        for model in models:
            choices.append((model.id, model.name))
        return choices


class Car(models.Model):

    carmodel = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=False)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)

    COLOR_UNKNOWN = 0
    WHITE = 1
    BLACK = 2
    RED = 3
    YELLOW = 4
    SILVER = 5

    COLOR_CHOICES = [
        (COLOR_UNKNOWN, 'Unkown'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
        (RED, 'Red'),
        (YELLOW, 'Yellow'),
        (SILVER, 'Silver')
    ]

    color = models.IntegerField(choices=COLOR_CHOICES, default=COLOR_UNKNOWN, null=False)

    GEAR_UNKNOWN = 0
    GEAR_AT = 1
    GEAR_MT = 2

    GEAR_CHOICES = [
        (GEAR_UNKNOWN, 'Unknown'),
        (GEAR_AT, 'AT'),
        (GEAR_MT, 'MT'),
    ]
    gear = models.IntegerField('TypeOfGear', choices=GEAR_CHOICES, default=GEAR_UNKNOWN, null=False)

    DRIVE_UNKNOWN = 0
    DRIVE_FF = 1
    DRIVE_FR = 2
    DRIVE_4WD = 3
    DRIVE_MR = 4

    DRIVE_CHOICES = [
        (DRIVE_UNKNOWN, 'Unknown'),
        (DRIVE_FF, 'FF'),
        (DRIVE_FR, 'FR'),
        (DRIVE_4WD, '4WD'),
        (DRIVE_MR, 'MIDSHIP'),
    ]
    drive = models.IntegerField('TypeOfDrive', choices=DRIVE_CHOICES, default=DRIVE_UNKNOWN, null=False)

    TYPE_SEDAN = 1
    TYPE_COUPE = 2
    TYPE_WAGON = 3
    TYPE_OPEN = 4
    TYPE_VAN = 4
    TYPE_ONEBOX = 5
    TYPE_TRUCK = 6
    BODY_TYPE_CHOICES = [
        (TYPE_SEDAN, 'SEDAN'),
        (TYPE_COUPE, 'COUPE'),
        (TYPE_WAGON, 'WAGON'),
    ]
    body_type = models.IntegerField('BodyType', choices=BODY_TYPE_CHOICES, default=DRIVE_UNKNOWN, null=False)

    model_year = models.PositiveIntegerField('model year', default=0)

    PLATE_CATEGORY_UNKNOWN = 0
    PLATE_CATEGORY_A = 1
    PLATE_CATEGORY_B = 2
    PLATE_CATEGORY_C = 3
    PLATE_CATEGORY_D = 4
    PLATE_CATEGORY_CHOICES = [
        (PLATE_CATEGORY_A, 'compact car'),
        (PLATE_CATEGORY_B, '5 numbers'),
        (PLATE_CATEGORY_C, '3 numbers'),
        (PLATE_CATEGORY_D, '8 numbers'),
    ]
    plate_category = models.IntegerField(choices=PLATE_CATEGORY_CHOICES, default=PLATE_CATEGORY_UNKNOWN, null=False)



    mileage = models.PositiveIntegerField('mileage', default=0)
    latest_inspection_date = models.DateField('LastInspectionDate', null=True)
    price = models.PositiveIntegerField('price', default=0)

    def get_color(self):
        return self.get_color_display()

    def get_gear(self):
        return self.get_gear_display()

    def get_body_type(self):
        return self.get_body_type_display()

    def get_drive(self):
        return self.get_drive_display()

    def get_plate_category(self):
        return self.get_plate_category_display()


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    picture = models.URLField()
    caption = models.TextField('説明')

    def __str__(self):
        return self.caption.text[:50]

    def __str__(self):
        return self.name
