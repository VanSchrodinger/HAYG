# Generated by Django 3.0.4 on 2020-03-25 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileserver', '0003_auto_20200325_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileinfo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 25, 10, 19, 42, 139517)),
        ),
    ]
