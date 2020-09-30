# Generated by Django 3.0.9 on 2020-09-24 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_order_installnote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='district',
            new_name='constituency',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='division',
            new_name='estate_village',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='employername',
            new_name='lr_num',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='estate',
            new_name='ward',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='housenum',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='province',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='staffnum',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='street',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='sublocation',
        ),
    ]
