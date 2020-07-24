from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


def validate_name(value, min=6, max=55):
    if len(value) < min or len(value) > max:
        raise ValidationError('Invalid product name')

def validate_value(value, min=0.0, max=99999.9):
    if value < min or value > max:
        raise ValidationError('Invalid value')

def validate_stock(value, min=0):
    if value < min :
        raise ValidationError('Invalid stock value')


class Product(models.Model):
  name = models.CharField(max_length=55, validators=[validate_name])
  value = models.FloatField(validators=[validate_value])
  discount_value = models.FloatField()
  stock = models.IntegerField(validators=[validate_stock])