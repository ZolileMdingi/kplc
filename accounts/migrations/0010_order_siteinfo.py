# Generated by Django 3.0.9 on 2020-08-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_order_appstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='siteinfo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
