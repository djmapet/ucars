from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return (self.name)


class CarModel(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type1 = [
    ('乗用自動車','３ナンバー'),
    ('小型乗用自動車','5ナンバー・７ナンバー'),#軽自動車も含む
    ('小型貨物自動車','４ナンバー'),
    ]
    type1 = models.CharField('車の分類1',max_length=11,choices=type1,)
    distinction_letter = models.CharField('判別文字',max_length=1)#「お」「し」「へ」「ん」は用いないこと
    registration_number = models.CharField('自動車登録番号',max_length=4)

    type2 = [
    ('sedan','セダン'),
    ('coupe','クーペ'),
    ('sports','スポーツカー'),
    ('station_wagon','ステーションワゴン'),
    ('hatchback','ハッチバック'),
    ('convertible','コンバーチブル'),
    ('suport_utility_vehicle','SUV'),
    ('minivan','ミニバン'),
    ('pickup_truck','トラック'),
    ]
    type2 = models.CharField('車の分類2',max_length=11,choices=type2,)

    type3 = [
    ('light','軽自動車'),
    ('nomal','自動車'),
    ]
    type3 = models.CharField('車の分類3'max_length=4,choices=type3,)

    def __str__(self):
        return (self.name)


class Car(models.Model):
    carmodel = models.ForeignKey(CarModel,on_delete=models.CASCADE)
    color = [
    ('Red','レッド'),
    ('Bleu','ブルー'),
    ('White','ホワイト'),
    ('Black','ブラック'),
    ('Yellow','イエロー'),
    ('Green','グリーン'),
    ('Decorated car','痛車'),
    ]
    color = models.CharField('車の色',max_length=15, choices=color,)

    car_repaired = [
        ('yes','修復歴有り'),
        ('no','修復歴無し'),
    ]
    car_repaired = models.CharField('修復歴',max_length=5, choices=car_repaired,)

    drive_system = [
        ('オートマ','AT・CVT'),
        ('マニュアル','MT'),
    ]
    drive_system = models.CharField('タイプ',max_length=6, choices=drive_system,)

    car_drive = [
        ('前輪駆動','FF'),
        ('後輪駆動','FR'),
        ('4輪駆動','4WD'),
        ('ミッドシップ','MR'),
        ]
    car_drive = models.CharField('駆動方式',max_length=6, choices=car_drive,)

    odometer1 = models.CharField('走行距離',max_length=7,)

    odometer2 = [
    ('50,000_or_less','5万キロ未満'),
    ('over_50,000','5万キロ以上'),
    ('over_100,000','10万キロ以上'),
    ]
    odometer2 = models.CharField('走行距離',max_length=14, choices=odometer2,)
