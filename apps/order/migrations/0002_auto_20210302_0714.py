# Generated by Django 2.2 on 2021-03-02 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='status_id',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='np_id',
            new_name='np',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='product_id',
            new_name='product',
        ),
    ]
