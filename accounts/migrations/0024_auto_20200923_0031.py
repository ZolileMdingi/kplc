# Generated by Django 3.0.9 on 2020-09-23 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_remove_customer_scf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='appstatus',
            field=models.CharField(blank=True, choices=[('No Application', 'No Application'), ('Under Review', 'Under Review'), ('Waiting for Qoute', 'Waiting for Qoute'), ('On Design', 'On Design'), ('Site visited', 'Site visited'), ('Installed', 'Installed')], max_length=200, null=True),
        ),
    ]
