# Generated by Django 3.1.2 on 2021-01-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20210128_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workloginfo',
            name='text',
            field=models.CharField(max_length=500, verbose_name='内容'),
        ),
    ]