# Generated by Django 3.2 on 2023-02-27 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Reviews'},
        ),
    ]