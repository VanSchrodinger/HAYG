#定义fileserver的URL模式
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns=[
    path('upload/', views.upload, name='upload'),  # 上传
    path('upload1/', views.upload1, name='upload1'),  # son上传
    path('new_folder/',views.new_folder,name='new_folder'),#新增文件夹
    path('new_folder1/',views.new_folder1,name='new_folder1'),#son新增文件夹
    path('list/<p>', views.list,name='list'),  # 列表
    path('move_list/<p>', views.move_list,name='move_list'),  # 列表
    path('list/son/<foler_name1>', views.list1,name='list1'),  # son列表edit_filename
    path('edit_filename/', views.edit_filename,name='edit_filename'),  # 重命名
    path('download/<id>', views.download, name='download'),  # 下载
    path('delete/<file_id>', views.delete, name='delete'),  # 删除n
    path('file_delete/', views.file_delete, name='file_delete'),  #删除1     
    path('delete_son/<file_id>', views.delete_son, name='delete_son'),  # 删除
    path('son_delete/', views.son_delete, name='son_delete'),  #删除1     
    path('1/', views.return_file, name='return_file'),  # 上一页 
    path('d2p/<file_id>', views.d2p, name='d2p'),  # 转换成pdf 
    path('post/<file_id>', views.post, name='post'),  #渲染 
    path('postlist/', views.postlist, name='postlist'),  # 批量
    path('postlist_son/', views.postlist_son, name='postlist_son'),  # 批量
    path('docx_ol/<file_id>',views.docx_ol,name='docx_ol'),
    path('test/',views.xq_c,name='test'),
    
]