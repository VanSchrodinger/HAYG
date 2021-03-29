#定义fileserver的URL模式
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns=[
    path('ot_list/', views.ot_list,name='ot_list'),#加班列表
    path('ot_search/', views.ot_search, name='ot_search'),  #加班查询
    path('add_ot/', views.add_ot, name='add_ot'),  # 登记加班
    path('ot_batch/', views.ot_batch, name='ot_batch'),  # 批量操作列表
    path('ot_update/', views.ot_update,name='ot_update'),#修改登记
    path('worklog/', views.worklog, name='worklog'),  # 日志列表
    # path('worklog_subordinate/', views.worklog_subordinate, name='worklog_subordinate'),  # 员工日志列表
    path('worklog_add/', views.worklog_add, name='worklog_add'),  # 新增日志
    path('worklog_update/', views.worklog_update, name='worklog_update'),  # 新增日志
    path('worklog_search/', views.worklog_search, name='worklog_search'),  #日志查询
    path('worklog_delete/', views.worklog_delete, name='worklog_delete'),  #日志删除
    path('worklog_export/', views.worklog_export, name='worklog_export'),  #日志导出
]