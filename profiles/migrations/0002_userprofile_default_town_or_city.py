# Generated by Django 3.2 on 2023-02-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_town_or_city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
