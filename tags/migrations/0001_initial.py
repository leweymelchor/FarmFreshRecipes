# Generated by Django 4.0.3 on 2023-04-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0003_alter_fooditem_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('recipes', models.ManyToManyField(related_name='tags', to='recipes.recipe')),
            ],
        ),
    ]
