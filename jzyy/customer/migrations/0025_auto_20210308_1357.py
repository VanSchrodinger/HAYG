# Generated by Django 3.1.2 on 2021-03-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0024_jobinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobinfo',
            name='create_date',
            field=models.CharField(max_length=500, verbose_name='创建日期'),
        ),
    ]