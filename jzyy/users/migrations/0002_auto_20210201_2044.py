# Generated by Django 3.1.2 on 2021-02-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.IntegerField(blank=True, choices=[(0, '部门总'), (1, '副总'), (2, '总助'), (3, '员工')], default=3, null=True, verbose_name='职级'),
        ),
    ]
