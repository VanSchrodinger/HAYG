from django.db import models
from django.utils import timezone

# CRM考试信息表
class CrmExamInfo(models.Model):
    name = models.CharField(verbose_name='答题人',max_length=500)
    user_code = models.IntegerField(verbose_name='账号')
    exam_name = models.CharField(max_length=500,verbose_name='活动名称')
    time_limit = models.IntegerField(verbose_name='时间限制（分钟）',default=60)
    times = models.CharField(max_length=500,default='无限制',verbose_name='可作答次数')
    real_times=models.IntegerField(default='1',verbose_name='实际次数')
    point=models.IntegerField(verbose_name='得分')
    create_date =models.DateTimeField(auto_now_add=True,verbose_name='创建时间',blank=True,null=True)

    # def __str__(self):
    #     return self.file_name
        #返回模型的字符串表示

# 扫描项无纸化信息表
class ScanInfo(models.Model):
    source_no = models.IntegerField(verbose_name='扫描项代码')#实际为source_no ，为方便migration用source_code
    source_name = models.CharField(verbose_name='扫描项名称',max_length=500)
    is_ecimc = models.CharField(verbose_name='是否无纸化',max_length=500)
    model_no = models.IntegerField(verbose_name='模板编号')
    app_id = models.CharField(verbose_name='渠道名称',max_length=500)
    busi_code = models.CharField(verbose_name='业务代码',max_length=500)
    busi_name = models.CharField(verbose_name='业务名称', max_length=500)
    cust_prop = models.IntegerField(verbose_name='机构类别')

# # 业务模板表
# class BusiServiceModel(models.Model):
#     model_no = models.IntegerField(verbose_name='模板编号')
#     app_id = models.IntegerField(verbose_name='渠道名称')
#     busi_code = models.IntegerField(verbose_name='业务代码')
#     cust_prop = models.IntegerField(verbose_name='机构类别')
#     in_active = models.IntegerField(verbose_name='是否使用')

# # 模板明细表
# class BusiModelDef(models.Model):
#     model_no = models.IntegerField(verbose_name='模板编号')
#     source_no = models.IntegerField(verbose_name='扫描项代码')    

# # 业务信息表
# class BusiCode(models.Model):
#     busi_code = models.IntegerField(verbose_name='业务代码')
#     busi_name = models.CharField(verbose_name='业务名称', max_length=500)
#     in_use = models.IntegerField(verbose_name='是否使用')
#     app_id = models.IntegerField(verbose_name='渠道名称')
    
