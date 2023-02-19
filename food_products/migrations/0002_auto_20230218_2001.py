# Generated by Django 3.2 on 2023-02-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodcategory',
            name='cat_img',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]