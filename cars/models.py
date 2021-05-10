from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True, unique=True, max_length=64)
    colour = models.CharField(verbose_name='Colour', max_length=64)
    brand = models.CharField(verbose_name='Brand', max_length=64)
    CAR_TYPES = (
        (1, 'Sedan'),
        (2, 'Hatchback'),
        (3, 'Universal'),
        (4, 'Coupe'),
        (5, 'Sedan'),
    )
    car_type = models.IntegerField(verbose_name='Brand', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
