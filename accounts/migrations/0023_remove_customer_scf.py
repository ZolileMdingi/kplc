# Generated by Django 3.0.9 on 2020-09-23 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_remove_customer_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='scf',
        ),
    ]
