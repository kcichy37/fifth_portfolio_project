# Generated by Django 3.2 on 2023-02-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodproduct',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
