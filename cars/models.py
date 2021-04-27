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

    SIZE_UNKNOWN = 0
    SIZE_3 = 1
    SIZE_5 = 2
    SIZE_4 = 3

    size = [
        (SIZE_UNKNOWN,'Unknown'),
        (SIZE_3,'3ナンバー'),
        (SIZE_5,'5ナンバー'),
        (SIZE_4,'4ナンバー'),
    ]
    size = models.IntegerField('車のサイズ',choices=size, default=SIZE_UNKNOWN, null=False)

    def __str__(self):
        return self.name


class Car(models.Model):
    carmodel = models.ForeignKey(CarModel,on_delete=models.CASCADE)
    register_shop = models.CharField('登録店舗',max_length=100,)
    shop_tel = models.CharField('電話番号',max_length=10,)
    shop_mailaddres = models.CharField('メールアドレス',max_length=100,)
    prefecture_UNKNOWN = 0 #都道府県の作成途中

    city = models.CharField('市',max_length=60,)
    area = models.CharField('区・町・村',max_length=60,)
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

    GEAR_UNKNOWN = 0
    GEAR_AT = 1
    GEAR_MT = 2

    GEAR_CHOICES = [
    (GEAR_UNKNOWN,'Unknown'),
    (GEAR_AT,'AT'),
    (GEAR_MT,'MT'),
    ]

    gear = models.IntegerField('ギアの種類',choices=GEAR_CHOICES, default=GEAR_UNKNOWN, null=False)



    DRIVE_UNKNOWN = 0
    DRIVE_FF = 1
    DRIVE_FR = 2
    DRIVE_4WD = 3
    DRIVE_MR = 4

    DRIVE_CHOICES = [
    (DRIVE_UNKNOWN,'Unknown'),
    (DRIVE_FF,'FF車'),
    (DRIVE_FR,'FR車'),
    (DRIVE_4WD,'4WD'),
    (DRIVE_MR,'ミッドシップ'),
    ]
    drive = models.IntegerField('駆動方式',choices=DRIVE_CHOICES, default=DRIVE_UNKNOWN, null=False)

    odometer = models.CharField('走行距離',max_length=7,)
    car_inspection_year = models.CharField('車検最終年',max_length=4,)
    car_inspection_month = models.CharField('車検最終月',max_length=2,)
    car_inspection_day = models.CharField('車検最終日',max_length=2,)

    def get_color(self):
        return  self.get_color_display()

class Image(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
