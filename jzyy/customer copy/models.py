from django.db import models
from django.utils import timezone


# # Create your models here.
class CustInfo(models.Model):
    cust_name = models.CharField(max_length=50,verbose_name='公司简称')
    cust_fullname = models.CharField(max_length=100,verbose_name='公司全称')
    invoice  = models.CharField(max_length=50,verbose_name='发票抬头',blank=True,null=True)
    profession = models.CharField(max_length=50,verbose_name='行业',choices = (('房地产', '房地产'),('互联网', '互联网'),('金融','金融')),blank=True,null=True)
    city = models.CharField(max_length=50,verbose_name='城市',choices = (('北京', '北京'),('上海', '上海'),('深圳','深圳')),blank=True,null=True)
    tel=models.CharField(max_length=50,verbose_name='电话',blank=True,null=True)
    website=models.URLField(max_length=50,verbose_name='网站',blank=True,null=True)
    location=models.CharField(max_length=50,verbose_name='地址',blank=True,null=True)
    email=models.EmailField(max_length=50,verbose_name='邮件',blank=True,null=True)
    finance =models.CharField(max_length=50,verbose_name='融资情况',blank=True,null=True)
    establish=models.CharField(max_length=50,verbose_name='成立时间',blank=True,null=True)
    source=models.CharField(max_length=50,verbose_name='来源',blank=True,null=True,choices = (('BD', 'BD'),('公司线索', '公司线索'),('内推','内推')))
    develop_stage=models.CharField(max_length=50,verbose_name='发展阶段',blank=True,null=True,choices = (('初创期', '初创期'),('快速成长期', '快速成长期'),('变革期','变革期'),('成熟期','成熟期'),('衰退期','衰退期')))
    salary_structure=models.CharField(max_length=50,verbose_name='薪资架构',blank=True,null=True)
    products =models.CharField(max_length=50,verbose_name='产品',blank=True,null=True)
    size=models.CharField(max_length=50,verbose_name='公司规模',blank=True,null=True)
    competitor=models.CharField(max_length=50,verbose_name='同行竞争者',blank=True,null=True)
    worktime=models.CharField(max_length=50,verbose_name='工作时间',blank=True,null=True)
    welfare1 =models.CharField(max_length=50,verbose_name='福利(保险、公积金)',blank=True,null=True)
    welfare2=models.CharField(max_length=50,verbose_name='福利(餐住车补)',blank=True,null=True)
    creator=models.CharField(max_length=50,verbose_name='创建人')
    nature=models.CharField(max_length=50,verbose_name='企业性质',blank=True,null=True,choices = (('央企', '央企'),('国企', '国企'),('民企','民企'),('合资','合资'),('外企','外企')))
    is_share =models.CharField(max_length=50,verbose_name='分享',blank=True,null=True,choices = (('是', '是'),('否', '否')))
    work_category=models.CharField(max_length=50,verbose_name='工作类别',blank=True,null=True,choices = (('1', '1'),('11', '11')))
    introduction=models.CharField(max_length=50,verbose_name='客户简介',blank=True,null=True)
    culture=models.CharField(max_length=50,verbose_name='企业文化',blank=True,null=True)
    interview_process=models.CharField(max_length=50,verbose_name='面试流程',blank=True,null=True)
    cust_style =models.CharField(max_length=50,verbose_name='客户类型',blank=True,null=True,choices = (('普通公司', '普通公司'),('开发中的客户', '开发中的客户'),('已签约的客户','已签约的客户'),('历史客户','历史客户'),('自动生成','自动生成')))
    value=models.CharField(max_length=50,verbose_name='公司年产值',blank=True,null=True)
    create_date =models.DateTimeField(auto_now_add=True,verbose_name='创建时间',blank=True,null=True)

    def __str__(self):
        return self.cust_name

class CustContact(models.Model):
    # cust = models.ForeignKey('CustInfo',to_field='cust_name',on_delete=models.CASCADE,verbose_name='客户名称')      
    cust = models.ForeignKey('CustInfo',on_delete=models.CASCADE,verbose_name='客户名称')  
    important = models.IntegerField(verbose_name='重要程度',default=0,choices=((0, '普通'),(1, 'vip')))
    contact_name = models.CharField(verbose_name='联系人姓名',max_length=50)
    position  = models.CharField(verbose_name='联系人职位',max_length=50,null=True,blank=True)
    contact_mobile = models.CharField(verbose_name='联系人手机',max_length=50,null=True,blank=True)
    contact_tel=models.CharField(verbose_name='联系人电话',max_length=50,null=True,blank=True)
    qq =models.CharField(verbose_name='联系人QQ',max_length=50,null=True,blank=True)
    wechat=models.CharField(verbose_name='微信',max_length=50,null=True,blank=True)
    gender = models.IntegerField(verbose_name='性别',default=0,null=True,blank=True,choices=((0, '男'),(1, '女')))
    birth=models.CharField(verbose_name='出生年月',max_length=50,null=True,blank=True)
    nation=models.CharField(verbose_name='籍贯',max_length=50,null=True,blank=True)
    tips=models.CharField(verbose_name='备注',max_length=50,null=True,blank=True)
    creator=models.CharField(verbose_name='创建人',null=True,blank=True,max_length=50)
    create_date =models.DateTimeField(auto_now_add=True,verbose_name='创建时间',blank=True,null=True)

#华安运管任务管理
class JobInfo(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    description = models.CharField(max_length=100,verbose_name='任务描述')
    create_date =models.DateTimeField(auto_now_add=True,verbose_name='创建日期',blank=True,null=True)
    creator=models.CharField(max_length=50,verbose_name='创建人')
    operator=models.CharField(max_length=50,verbose_name='经办人')
    status = models.CharField(max_length=50,verbose_name='状态',choices = (('跟踪中', '跟踪中'),('完成', '完成'),('作废','作废')),blank=True,null=True)
    
    def __str__(self):
        return self.title
    

  

    