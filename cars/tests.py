from django.test import TestCase

# Create your tests here.

from cars.models import Manufacturer, CarModel, Car, Shop


def create_maker():
    maker = Manufacturer(name="TOYOTA")
    maker.save()
    return maker


def create_car_model(maker):
    car_model = CarModel(name="Prius")
    car_model.id = 1
    car_model.manufacturer = maker
    car_model.save()
    return car_model


class CarModelTests(TestCase):
    def setUp(self):
        self.maker = create_maker()
        self.car_model = create_car_model(self.maker)

    def test_white_color(self):
        car = Car()
        car.color = car.WHITE
        car.carmodel = self.car_model
        car.save()

        self.assertEqual(car.color, 1)
        self.assertEqual(car.get_color_display(), 'White')

    def test_unkown_color(self):
        car = Car()
        car.carmodel = self.car_model
        car.save()

        self.assertEqual(car.color, 0)
        self.assertEqual(car.get_color(), 'Unkown')


class ShopTests(TestCase):
    def setUp(self):
        pass

    def test_pref(self):
        shop = Shop(name="aaa", tel="03-111-3333", email="hoge@hoge.com", city="kawasaki", area="???")
        shop.pref = 13
        shop.save()

        self.assertEqual(shop.pref, 13)
        self.assertEqual(shop.get_pref(), '東京')

class CarTests(TestCase):
    def setUp(self):
        self.maker = create_maker()
        self.car_model = create_car_model(self.maker)

    def test_car_gear(self):
        car1 = Car()
        car1.carmodel = self.car_model
        car1.gear = Car.GEAR_AT
        car1.save()

        car2 = Car()
        car2.carmodel = self.car_model
        car2.gear = Car.GEAR_MT
        car2.save()

        car3 = Car()
        car3.carmodel = self.car_model
        car3.save()

        all_cars = Car.objects.all()
        self.assertEqual(len(all_cars), 3)

        at_cars = Car.objects.filter(gear=Car.GEAR_AT)
        self.assertEqual(len(at_cars), 1)
        self.assertEqual(at_cars[0], car1)

        mt_cars = Car.objects.filter(gear=Car.GEAR_MT)
        self.assertEqual(len(mt_cars), 1)
        self.assertEqual(mt_cars[0], car2)

        unknown_cars = Car.objects.filter(gear=Car.GEAR_UNKNOWN)
        self.assertEqual(len(unknown_cars), 1)
        self.assertEqual(unknown_cars[0], car3)