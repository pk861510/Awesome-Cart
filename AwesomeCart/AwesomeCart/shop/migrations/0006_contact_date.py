# Generated by Django 5.0.6 on 2024-07-18 02:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_contact_phone_number_contact_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 7, 18, 7, 47, 9, 952787)),
        ),
    ]
