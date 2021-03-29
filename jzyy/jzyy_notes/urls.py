#定义jzyy_notes的URL模式
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns=[
    #主页
    path('', views.index, name='index'),
    path('topics/<num>', views.topics, name='topics'),
    # path('new_public/',views.new_public,name='new_public'), 
    # path('public/',views.public,name='public'),           
    path('topic/<topic_id>',views.topic,name='topic'),
    path('edit_topic/',views.edit_topic,name='edit_topic'),
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/<topic_id>',views.new_entry,name='new_entry'),
    path('edit_entry/',views.edit_entry,name='edit_entry'),
    path('search/',views.search,name='search'),
    # path('qa/',views.qa,name='qa'),
    # path('new_qa/',views.new_qa,name='new_qa'),
]