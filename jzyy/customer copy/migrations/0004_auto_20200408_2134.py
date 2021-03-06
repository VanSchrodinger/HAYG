# Generated by Django 3.0.4 on 2020-04-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20200408_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custinfo',
            name='city',
            field=models.IntegerField(default=0, null=True, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='creator',
            field=models.IntegerField(default=0, null=True, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='develop_stage',
            field=models.IntegerField(default=0, null=True, verbose_name='发展阶段'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='is_share',
            field=models.IntegerField(default=0, null=True, verbose_name='分享'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='nature',
            field=models.CharField(max_length=50, null=True, verbose_name='企业性质'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='profession',
            field=models.IntegerField(default=0, null=True, verbose_name='行业'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='source',
            field=models.IntegerField(default=0, null=True, verbose_name='来源'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='work_category',
            field=models.IntegerField(default=0, null=True, verbose_name='工作类别'),
        ),
    ]
