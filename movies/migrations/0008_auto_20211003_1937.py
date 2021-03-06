# Generated by Django 3.2.7 on 2021-10-03 19:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20211003_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='saved_date',
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                null=True
            ),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='viewed_date',
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now
            ),
        ),
    ]
