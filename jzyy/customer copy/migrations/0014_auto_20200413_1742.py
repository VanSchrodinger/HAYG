# Generated by Django 3.0.4 on 2020-04-13 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_auto_20200413_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custcontact',
            name='cust',
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='cust_name',
            field=models.CharField(max_length=50, verbose_name='公司简称'),
        ),
    ]
