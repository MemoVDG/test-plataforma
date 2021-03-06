# Generated by Django 3.0.8 on 2020-07-24 04:04

from django.db import migrations, models
import productos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, validators=[productos.models.validate_name])),
                ('value', models.FloatField(validators=[productos.models.validate_value])),
                ('discount_value', models.FloatField()),
                ('stock', models.IntegerField(validators=[productos.models.validate_stock])),
            ],
        ),
    ]
