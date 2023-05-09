# Generated by Django 4.0.3 on 2023-05-09 02:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_alter_rating_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
