# Generated by Django 3.0.9 on 2020-09-27 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_auto_20200925_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appliancename', models.CharField(blank=True, choices=[('Kettle', 'Kettle'), ('Fridge', 'Fridge'), ('TV', 'TV'), ('Other', 'Other')], max_length=200, null=True)),
                ('consumption', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('units', models.CharField(blank=True, default='Kwh', max_length=200, null=True)),
                ('num_appliances', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='appliances',
            field=models.ManyToManyField(to='accounts.Appliance'),
        ),
    ]
