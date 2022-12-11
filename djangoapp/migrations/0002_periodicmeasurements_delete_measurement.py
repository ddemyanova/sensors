# Generated by Django 4.1.3 on 2022-12-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodicMeasurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pressure', models.DecimalField(decimal_places=2, max_digits=7)),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Measurement',
        ),
    ]
