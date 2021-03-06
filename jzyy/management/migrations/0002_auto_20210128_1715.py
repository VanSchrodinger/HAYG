# Generated by Django 3.1.2 on 2021-01-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorklogInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=500, verbose_name='日期')),
                ('text', models.CharField(max_length=500, verbose_name='加班人员')),
                ('user', models.CharField(max_length=500, verbose_name='用户名')),
            ],
        ),
        migrations.AlterField(
            model_name='overtimeinfo',
            name='expense',
            field=models.IntegerField(default=60, verbose_name='餐费支出'),
        ),
    ]
