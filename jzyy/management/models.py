from django.db import models
from django.utils import timezone

# 加班登记表
class OvertimeInfo(models.Model):
    date = models.CharField(verbose_name='加班日期',max_length=500)
    work_type = models.CharField(verbose_name='加班类型',max_length=500,default='周末测试',choices=(('工作日加班', '工作日加班'),('周末测试', '周末测试')))
    work_info = models.CharField(verbose_name='加班事项',max_length=500)
    name = models.CharField(verbose_name='加班人员',max_length=500)
    expense = models.IntegerField(verbose_name='餐费支出',default=60)
    extra = models.CharField(max_length=500,verbose_name='补充说明',default='无')

# 工作日志表
class WorklogInfo(models.Model):
    date = models.CharField(verbose_name='日期',max_length=500)
    text = models.CharField(verbose_name='内容',max_length=500)
    user = models.CharField(max_length=500,verbose_name='用户名')
    