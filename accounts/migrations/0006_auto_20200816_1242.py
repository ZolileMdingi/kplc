# Generated by Django 3.0.9 on 2020-08-16 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200816_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='productx',
            new_name='product',
        ),
    ]
