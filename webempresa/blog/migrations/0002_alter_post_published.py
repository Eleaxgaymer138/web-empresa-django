# Generated by Django 5.1.1 on 2024-09-27 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 27, 22, 49, 6, 993599, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicacion'),
        ),
    ]
