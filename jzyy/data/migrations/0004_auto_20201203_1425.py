# Generated by Django 3.1.2 on 2020-12-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20201202_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScanInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_code', models.IntegerField(verbose_name='扫描项代码')),
                ('source_name', models.CharField(max_length=500, verbose_name='扫描项名称')),
                ('is_ecimc', models.CharField(max_length=500, verbose_name='是否无纸化')),
                ('model_no', models.IntegerField(verbose_name='模板编号')),
                ('app_id', models.IntegerField(verbose_name='渠道名称')),
                ('busi_code', models.IntegerField(verbose_name='业务代码')),
                ('busi_name', models.CharField(max_length=500, verbose_name='业务名称')),
                ('cust_prop', models.IntegerField(verbose_name='机构类别')),
            ],
        ),
        migrations.DeleteModel(
            name='BusiCode',
        ),
        migrations.DeleteModel(
            name='BusiModelDef',
        ),
        migrations.DeleteModel(
            name='BusiServiceModel',
        ),
        migrations.DeleteModel(
            name='SourceScanInfo',
        ),
    ]
