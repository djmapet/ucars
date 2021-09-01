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


class Car(models.Model):
    CAR_UNKNOWN = 0
    #TOYOTA = 1
    #NISSAN = 2
    #HONDA = 3
    #MAZDA = 4
    #MITSUBISHI = 5
    #SUBARU = 6
    #SUZUKI = 7
    #DAIHATSU = 8
    #PORSCHE = 9
    #MERCEDES = 10
    #BMW = 11
    PRIUS = 1
    SKYLINE = 2
    MR2 = 3
    HIGHACE = 4
    CX5 = 5
    S2000 = 6
    IMPREZASti = 7
    PAJERO = 8
    JIMNY = 9
    COROLA = 10
    E30 = 11
    ヴィッツ = 12
    ポルシェ911 = 13
    ベンツSクラス = 14
    ベンツG350dヘリテージ = 15
    アトレーワゴン = 16
    コペンセロ = 17
    フォレスター = 18
    NOAH = 19
    ハチロク = 20

    CARMODEL_CHOICES = [
        (CAR_UNKNOWN, 'Unknown'),
        #(TOYOTA, 'トヨタ'),
        #(NISSAN, '日産'),
        #(HONDA, 'ホンダ'),
        #(MAZDA, 'マツダ'),
        #(MITSUBISHI, '三菱'),
        #(SUBARU, 'スバル'),
        #(SUZUKI, 'スズキ'),
        #(DAIHATSU, 'ダイハツ'),
        #(PORSCHE, 'ポルシェ'),
        #(MERCEDES, 'メルセデス'),
        #(BMW, 'BMW'),
        (1, 'PRIUS'),
        (2, 'SKYLINE'),
        (3, 'MR-2'),
        (4, 'HIGH-ACE'),
        (5, 'CX-5'),
        (6, 'S2000'),
        (7, 'IMPREZA Sti'),
        (8, 'PAJERO'),
        (9, 'JIMNY'),
        (10, 'COROLA'),
        (11, 'E30'),
        (12, 'ヴィッツ'),
        (13, 'ポルシェ911'),
        (14, 'ベンツSクラス'),
        (15, 'ベンツG350d ヘリテージ'),
        (16, 'アトレーワゴン'),
        (17, 'コペンセロ'),
        (18, 'フォレスター'),
        (19, 'NOAH'),
        (20, 'ハチロク'),
    ]
    carmodel = models.ForeignKey(CarModel, on_delete=models.CASCADE,choices=CARMODEL_CHOICES, null=False)


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
