#为应用程序users定义url模式
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns=[
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register'),
    path('change_pw/',PasswordChangeView.as_view(template_name='users/change_pw.html',
        success_url='/users/change_pwd/'),name='change_pw'),
    path('change_pwd/',PasswordChangeDoneView.as_view(template_name = 'users/change_pwd.html'),
         name='change_pwd'),
]