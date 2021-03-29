from django.db import models
from django.utils import timezone

# Create your models here.
class FileInfo(models.Model):
    file_name = models.CharField(max_length=500)
    file_size = models.DecimalField(max_digits=10, decimal_places=0,default=0)
    file_path = models.CharField(max_length=500)
    upload_time = models.DateTimeField(default=timezone.now)
    file_type = models.CharField(max_length=500,default='FOLDER')
    load_user=models.CharField(max_length=500)
    is_personal=models.IntegerField(default=0)
    folder_name=models.CharField(max_length=500)

    # def filename_len(self):
    #     if len(str(self.file_name))>30:
    #         return '{}...'.format(str(self.file_name)[0:30])
    #     else:
    #         return str(self.file_name)
    # filename_len.allow_tags = True

    # def __str__(self):
    #     return self.file_name
        #返回模型的字符串表示

class Xqtj(models.Model):
    work_id = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    tj_path = models.CharField(max_length=500)
    