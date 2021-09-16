# Generated by Django 3.2.7 on 2021-09-16 08:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('imdb_id', models.PositiveIntegerField(default=None)),
                ('title', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField()),
                ('picture', models.TextField(null=True)),
                ('plot', models.TextField()),
                ('cast', models.ManyToManyField(related_name='cast', to='movies.Person')),
                ('category', models.ManyToManyField(to='movies.Category')),
                ('country', models.ManyToManyField(to='movies.Country')),
                ('director', models.ManyToManyField(related_name='director', to='movies.Person')),
            ],
        ),
    ]
