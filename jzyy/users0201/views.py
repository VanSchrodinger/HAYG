from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import User
from .decorate import MenuHelper

  
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('jzyy_notes:index'))

# 注册
def register(request):
    if request.method != 'POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            authenticated_user=authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('jzyy_notes:index'))

    context={'form':form}
    return render(request,'users/register.html',context)

#登陆
def login(request):
    if request.method == "GET":
        return render(request, 'users/login.html')
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        obj = User.objects.filter(username=username, password=pwd).first()
        if obj:
            # 登录成功，获取当前用户信息
            # 放到session中
            request.session['user_info'] = {'nid': obj.id, 'username': obj.username}
            # 获取当前用户的所有权限，获取所有菜单，获取在菜单中显示的权限（叶子节点）
            # 放到session中
            MenuHelper(request, obj.username)
            return HttpResponseRedirect(reverse('jzyy_notes:index'))
        else:
            return HttpResponseRedirect(reverse('users:login'))