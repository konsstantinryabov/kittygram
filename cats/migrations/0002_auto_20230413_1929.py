# Generated by Django 3.2 on 2023-04-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterModelTable(
            name='cat',
            table='cats',
        ),
    ]
