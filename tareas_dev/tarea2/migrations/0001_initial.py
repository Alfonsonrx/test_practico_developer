# Generated by Django 4.1.7 on 2023-02-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=150)),
                ('tipo', models.CharField(max_length=5)),
                ('region', models.CharField(max_length=30)),
                ('tipologia', models.CharField(max_length=4)),
                ('titular', models.CharField(max_length=150)),
                ('inversion', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fecha_ingreso', models.DateTimeField()),
                ('estado', models.CharField(max_length=150)),
            ],
        ),
    ]
