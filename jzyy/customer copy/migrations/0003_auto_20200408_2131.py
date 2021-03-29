# Generated by Django 3.0.4 on 2020-04-08 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200408_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custinfo',
            name='city',
            field=models.IntegerField(default=0, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='competitor',
            field=models.CharField(max_length=50, null=True, verbose_name='同行竞争者'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='creator',
            field=models.CharField(max_length=50, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='culture',
            field=models.CharField(max_length=50, null=True, verbose_name='企业文化'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='cust_fullname',
            field=models.CharField(max_length=100, verbose_name='公司全称'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='cust_name',
            field=models.CharField(max_length=50, verbose_name='公司简称'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='cust_style',
            field=models.IntegerField(default=0, null=True, verbose_name='客户类型'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='develop_stage',
            field=models.IntegerField(default=0, verbose_name='发展阶段'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='email',
            field=models.CharField(max_length=50, null=True, verbose_name='邮件'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='establish',
            field=models.CharField(max_length=50, null=True, verbose_name='成立时间'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='finance',
            field=models.CharField(max_length=50, null=True, verbose_name='融资情况'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='interview_process',
            field=models.CharField(max_length=50, null=True, verbose_name='面试流程'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='introduction',
            field=models.CharField(max_length=50, null=True, verbose_name='客户简介'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='invoice',
            field=models.CharField(max_length=50, null=True, verbose_name='发票抬头'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='is_share',
            field=models.IntegerField(default=0, verbose_name='分享'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='location',
            field=models.CharField(max_length=50, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='nature',
            field=models.CharField(max_length=50, verbose_name='企业性质'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='products',
            field=models.CharField(max_length=50, null=True, verbose_name='产品'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='profession',
            field=models.IntegerField(default=0, verbose_name='行业'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='salary_structure',
            field=models.CharField(max_length=50, null=True, verbose_name='薪资架构'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='size',
            field=models.CharField(max_length=50, null=True, verbose_name='公司规模'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='source',
            field=models.IntegerField(default=0, verbose_name='来源'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='tel',
            field=models.CharField(max_length=50, null=True, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='value',
            field=models.CharField(max_length=50, null=True, verbose_name='公司年产值'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='website',
            field=models.CharField(max_length=50, null=True, verbose_name='网站'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='welfare1',
            field=models.CharField(max_length=50, null=True, verbose_name='福利(保险、公积金)'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='welfare2',
            field=models.CharField(max_length=50, null=True, verbose_name='福利(餐住车补)'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='work_category',
            field=models.CharField(max_length=50, verbose_name='工作类别'),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='worktime',
            field=models.CharField(max_length=50, null=True, verbose_name='工作时间'),
        ),
    ]