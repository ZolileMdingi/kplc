# Generated by Django 3.0.9 on 2020-09-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_order_siteinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='agreebtn',
            field=models.CharField(choices=[('YES I AGREE', 'YES I AGREE'), ('NO I DO NOT AGREE', 'NO I DO NOT AGREE')], max_length=200, null=True),
        ),
    ]