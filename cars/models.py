from django.db import models
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


class Pref(models.Model):
    PREF_CHOICES = [
        (1, '北海道'),
        (2, '青森'),
        (3, '岩手'),
        (4, '宮城'),
        (5, '秋田'),
        (6, '山形'),
        (7, '福島'),
        (8, '茨城'),
        (9, '栃木'),
        (10, '群馬'),
        (11, '埼玉'),
        (12, '千葉'),
        (13, '東京'),
        (14, '神奈川'),
        (15, '新潟'),
        (16, '富山'),
        (17, '石川'),
        (18, '福井'),
        (19, '山梨'),
        (20, '長野'),
        (21, '岐阜'),
        (22, '静岡'),
        (23, '愛知'),
        (24, '三重'),
        (25, '滋賀'),
        (26, '京都'),
        (27, '大阪'),
        (28, '兵庫'),
        (29, '奈良'),
        (30, '和歌山'),
        (31, '鳥取'),
        (32, '島根'),
        (33, '岡山'),
        (34, '広島'),
        (35, '山口'),
        (36, '徳島'),
        (37, '香川'),
        (38, '愛媛'),
        (39, '高知'),
        (40, '福岡'),
        (41, '佐賀'),
        (42, '長崎'),
        (43, '熊本'),
        (44, '大分'),
        (45, '宮崎'),
        (46, '鹿児島'),
        (47, '沖縄')
    ]


class Shop(models.Model):
    tel_number_regex = RegexValidator(regex=r'^[0-9\-]+$', message="Phone number must be up to 15 digits and '-' allowed.")
    name = models.CharField('shop name', max_length=100)
    tel = models.CharField('telephon number', validators=[tel_number_regex], max_length=15)
    email = models.EmailField('email', max_length=100, null=True)

    pref = models.IntegerField(choices=Pref.PREF_CHOICES)
    city = models.CharField('City', max_length=20)
    area = models.CharField('Area', max_length=20)

    def __str__(self):
        return self.name

    def get_pref(self):
        return self.get_pref_display()


class Car(models.Model):
    carmodel = models.ForeignKey(CarModel, on_delete=models.CASCADE)
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
        (TYPE_SEDAN, 'Sedan'),
        (TYPE_COUPE, 'COUPE'),
        (TYPE_WAGON, 'Wagon'),
    ]
    body_type = models.IntegerField('BodyType', choices=DRIVE_CHOICES, default=DRIVE_UNKNOWN, null=False)

    model_year = models.PositiveIntegerField('model year', null=True)

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

    def get_color(self):
        return self.get_color_display()


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    picture = models.URLField()
