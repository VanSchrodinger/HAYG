from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32,verbose_name='用户名')
    level = models.IntegerField(verbose_name='职级',choices = ((0, '部门总'),(1, '副总'),(2, '总助'),(3,'员工')),blank=True,null=True,default=3)
    leader = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='领导') 


    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.username


class Role(models.Model):
    role = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = '角色表'

    def __str__(self):
        return self.role


class User2Role(models.Model):
    u = models.ForeignKey(User, on_delete=models.CASCADE)
    r = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '用户分配角色'

    def __str__(self):
        return '%s-%s' % (self.u.username, self.r.role)


class Menu(models.Model):
    caption = models.CharField(max_length=32)
    parent = models.ForeignKey('self', related_name='p', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.caption,)


class Permission(models.Model):
    caption = models.CharField(max_length=32)
    url = models.CharField(max_length=32)
    menu = models.ForeignKey(Menu, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'URL表'

    def __str__(self):
        return '%s-%s' % (self.caption, self.url)


class Action(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = '操作表'

    def __str__(self):
        return self.caption


class Permission2Action(models.Model):
    p = models.ForeignKey(Permission, on_delete=models.CASCADE)
    a = models.ForeignKey(Action, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '权限表'

    def __str__(self):
        return '%s-%s:-%s?t=%s' % (self.p.caption, self.a.caption, self.p.url, self.a.code)


class Permission2Action2Role(models.Model):
    p2a = models.ForeignKey(Permission2Action, on_delete=models.CASCADE)
    r = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '角色分配权限'

    def __str__(self):
        return '%s=>%s' % (self.r.role, self.p2a)