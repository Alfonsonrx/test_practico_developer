# Generated by Django 4.1.7 on 2023-02-17 07:53

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('empty_slots', models.IntegerField()),
                ('free_bikes', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=20)),
                ('name', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('uid', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('altitude', models.DecimalField(decimal_places=1, max_digits=10)),
                ('ebikes', models.IntegerField()),
                ('has_ebikes', models.BooleanField(default=True)),
                ('last_updated', models.IntegerField()),
                ('normal_bikes', models.IntegerField()),
                ('payment', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=5)),
                ('payment_terminal', models.BooleanField()),
                ('post_code', models.CharField(blank=True, max_length=10)),
                ('renting', models.IntegerField()),
                ('returning', models.IntegerField()),
                ('slots', models.IntegerField()),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarea1.station')),
            ],
        ),
    ]
