#定义fileserver的URL模式
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns=[
    path('add/', views.add_cust, name='add_cust'),  # 新增客户
    path('add_job/', views.add_job, name='add_job'),  # 新增任务
    path('add1/', views.add_contact, name='add_contact'),  # 新增客户联系人
    path('edit_contact/<contact_id>', views.edit_contact, name='edit_contact'),  # 修改客户联系人
    path('jobinfo/', views.jobinfo, name='jobinfo'),  # 列表
    path('custinfo/<cust_id>', views.custdetails, name='custdetails'),  # 客户详细信息
    path('edit_info/<cust_id>', views.edit_info, name='edit_info'),  # 编辑客户信息
    path('cust_search/', views.custsearch, name='custsearch'),  # 客户搜索
    path('contact_op/', views.contact_operation, name='contact_operation'),  # 客户搜索
  
]