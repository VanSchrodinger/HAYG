# Generated by Django 3.0.4 on 2020-04-13 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_auto_20200413_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custcontact',
            name='cust',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustInfo'),
        ),
    ]
