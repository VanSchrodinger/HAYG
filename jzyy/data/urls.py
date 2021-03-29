#定义fileserver的URL模式
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns=[
    path('list/', views.list,name='list'),
    path('shine/', views.shine,name='shine'),#无纸化率
    path('input/', views.input, name='input'),  # 上传加载
    path('input_shine/', views.input_shine, name='input_shine'),  # 上传shine加载
    path('crmsearch/', views.crmsearch, name='crmsearch'),  # 客户搜索
    path('shinesearch/', views.shinesearch, name='shinesearch'),  # 客户搜索
    path('add_crm/', views.add_crm, name='add_crm'),  # 新增考试成绩
    path('batch/', views.batch, name='batch'),  # 批量操作列表
]