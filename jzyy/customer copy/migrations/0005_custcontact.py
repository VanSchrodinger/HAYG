# Generated by Django 3.0.4 on 2020-04-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20200408_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('important', models.IntegerField(choices=[(0, '普通'), (1, 'vip')], default=0, verbose_name='重要程度')),
                ('contact_name', models.CharField(max_length=50, verbose_name='联系人姓名')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='联系人职位')),
                ('contact_mobile', models.CharField(blank=True, max_length=50, null=True, verbose_name='联系人手机')),
                ('contact_tel', models.CharField(blank=True, max_length=50, null=True, verbose_name='联系人电话')),
                ('qq', models.CharField(blank=True, max_length=50, null=True, verbose_name='联系人QQ')),
                ('wechat', models.CharField(blank=True, max_length=50, null=True, verbose_name='微信')),
                ('gender', models.IntegerField(blank=True, choices=[(0, '男'), (1, '女')], default=0, null=True, verbose_name='性别')),
                ('birth', models.CharField(blank=True, max_length=50, null=True, verbose_name='出生年月')),
                ('nation', models.CharField(blank=True, max_length=50, null=True, verbose_name='籍贯')),
                ('tips', models.CharField(blank=True, max_length=50, null=True, verbose_name='备注')),
                ('creator', models.IntegerField(blank=True, choices=[(0, 'wansx'), (1, 'zhoulele')], default=0, null=True, verbose_name='创建人')),
            ],
        ),
    ]
