# Generated by Django 3.0.4 on 2020-04-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20200413_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custinfo',
            name='city',
            field=models.CharField(blank=True, choices=[('普通公司', '普通公司'), ('开发中的客户', '开发中的客户'), ('已签约的客户', '已签约的客户'), ('历史客户', '历史客户'), ('自动生成', '自动生成')], max_length=50, null=True, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='creator',
            field=models.CharField(blank=True, choices=[('普通公司', '普通公司'), ('开发中的客户', '开发中的客户'), ('已签约的客户', '已签约的客户'), ('历史客户', '历史客户'), ('自动生成', '自动生成')], max_length=50, null=True, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='develop_stage',
            field=models.CharField(blank=True, choices=[('普通公司', '普通公司'), ('开发中的客户', '开发中的客户'), ('已签约的客户', '已签约的客户'), ('历史客户', '历史客户'), ('自动生成', '自动生成')], max_length=50, null=True, verbose_name='发展阶段'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='is_share',
            field=models.CharField(blank=True, choices=[('普通公司', '普通公司'), ('开发中的客户', '开发中的客户'), ('已签约的客户', '已签约的客户'), ('历史客户', '历史客户'), ('自动生成', '自动生成')], max_length=50, null=True, verbose_name='分享'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='nature',
            field=models.CharField(blank=True, choices=[('普通公司', '普通公司'), ('开发中的客户', '开发中的客户'), ('已签约的客户', '已签约的客户'), ('历史客户', '历史客户'), ('自动生成', '自动生成')], max_length=50, null=True, verbose_name='企业性质'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='profession',
            field=models.CharField(blank=True, choices=[('普通公司', '普通公司'), ('开发中的客户', '开发中的客户'), ('已签约的客户', '已签约的客户'), ('历史客户', '历史客户'), ('自动生成', '自动生成')], max_length=50, null=True, verbose_name='行业'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='source',
            field=models.CharField(blank=True, choices=[('普通公司', '普通公司'), ('开发中的客户', '开发中的客户'), ('已签约的客户', '已签约的客户'), ('历史客户', '历史客户'), ('自动生成', '自动生成')], max_length=50, null=True, verbose_name='来源'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='work_category',
            field=models.CharField(blank=True, choices=[('普通公司', '普通公司'), ('开发中的客户', '开发中的客户'), ('已签约的客户', '已签约的客户'), ('历史客户', '历史客户'), ('自动生成', '自动生成')], max_length=50, null=True, verbose_name='工作类别'),
        ),
    ]
