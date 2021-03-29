from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
# 用户学习的主题
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    is_personal=models.IntegerField(default=0)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text
        #返回模型的字符串表示

class Entry(models.Model):
    #某个主题的具体知识
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    title=models.TextField()
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='entries'

    def __str__(self):
        #返回模型的字符串表示
        return self.text[:30]+'...'

# 风险管理监控信息维护表
class Equipmentinfo(models.Model):
    name = models.CharField(max_length=500)
    id_code = models.CharField(max_length=500)
    outer_ip = models.CharField(max_length=500)
    py_address = models.CharField(max_length=500)
    tel = models.CharField(max_length=500)
    mobile=models.CharField(max_length=500)

    # def __str__(self):
    #     return self.file_name
        #返回模型的字符串表示

