# Generated by Django 2.2 on 2021-03-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20210302_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='emails',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]