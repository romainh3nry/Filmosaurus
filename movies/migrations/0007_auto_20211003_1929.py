# Generated by Django 3.2.7 on 2021-10-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20211003_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='saved_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='viewed_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
