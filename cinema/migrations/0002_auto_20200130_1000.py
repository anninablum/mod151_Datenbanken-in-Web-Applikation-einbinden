# Generated by Django 3.0.2 on 2020-01-30 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cinema_movie',
            name='fk_cinema',
        ),
        migrations.RemoveField(
            model_name='cinema_movie',
            name='fk_movie',
        ),
    ]