# Generated by Django 3.1.2 on 2021-03-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0023_auto_20200424_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('description', models.CharField(max_length=100, verbose_name='任务描述')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建日期')),
                ('creator', models.CharField(max_length=50, verbose_name='创建人')),
                ('operator', models.CharField(max_length=50, verbose_name='经办人')),
                ('status', models.CharField(blank=True, choices=[('跟踪中', '跟踪中'), ('完成', '完成'), ('作废', '作废')], max_length=50, null=True, verbose_name='状态')),
            ],
        ),
    ]