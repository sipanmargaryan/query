# Generated by Django 2.2 on 2021-03-02 06:59

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('email_address', models.CharField(max_length=256)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
