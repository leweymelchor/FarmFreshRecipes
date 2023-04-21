# Generated by Django 4.0.3 on 2023-04-21 18:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
