# Generated by Django 3.2 on 2023-02-23 21:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("enquiries", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enquiry",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
