from django.db import models
from django.core.validators import RegexValidator
from .common import Pref

class Shop(models.Model):
    tel_number_regex = RegexValidator(regex=r'^[0-9\-]+$', message="Phone number must be up to 15 digits and '-' allowed.")
    email_regex = RegexValidator(regex=r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", message="bad email format.")

    name = models.CharField('shop name', max_length=100)
    tel = models.CharField('telephon number', validators=[tel_number_regex], max_length=15)
    email = models.EmailField('email', validators=[email_regex], max_length=100, null=True)

    pref = models.IntegerField(choices=Pref.PREF_CHOICES)
    city = models.CharField('City', max_length=20)
    area = models.CharField('Area', max_length=20)

    def __str__(self):
        return self.name

    def get_pref(self):
        return self.get_pref_display()
