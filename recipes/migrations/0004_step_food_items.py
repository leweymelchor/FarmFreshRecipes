# Generated by Django 4.0.3 on 2023-04-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_fooditem_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='food_items',
            field=models.ManyToManyField(blank=True, null=True, to='recipes.fooditem'),
        ),
    ]