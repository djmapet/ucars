from django.test import TestCase

# Create your tests here.

from cars.models import Manufacturer, CarModel, Car

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
