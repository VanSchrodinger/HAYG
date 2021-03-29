from django.shortcuts import render
from django.http import HttpResponseRedirect,FileResponse,HttpResponse
from django.template import RequestContext
from django.urls import reverse
from django.utils.http import urlquote
from .models import OvertimeInfo,WorklogInfo
from django.db.models import Q
from .forms import OtForm,OtSearchForm,OtForm1,WlForm,WlForm1,WlSearchForm,UlForm
import os,stat,shutil,sys,win32com.client
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import get_user
from django.contrib.auth.models import User
import pythoncom
from pydocx import PyDocX
from PyPDF2 import PdfFileReader, PdfFileWriter
import time,xlrd,pymysql
from django.contrib import messages
import pandas as pd
from sqlalchemy import create_engine
from tkinter import messagebox
import json
import django_excel
import pyautogui  #鼠标键盘控制，弃用
    


# 加班登记列表
@login_required
def ot_list(request):
    if request.method != "POST":
        form = OtForm(label_suffix='')
        form1 =OtSearchForm(label_suffix='')
        form2 = OtForm1(label_suffix='')
    else:
        form = OtForm(request.POST)
        if form.is_valid():
            ot = OvertimeInfo(date=form.cleaned_data['date'], 
                        work_type=form.cleaned_data['work_type'],
                        work_info = form.cleaned_data['work_info'],
                        name = form.cleaned_data['name'],
                        expense = form.cleaned_data['expense'],
                        extra=form.cleaned_data['extra'])
            ot.save()
            return HttpResponseRedirect(reverse('management:ot_list'))
        else:
            print('不合法的表格')

    ot_infos=OvertimeInfo.objects.filter().order_by('-date')
    paginator = Paginator(ot_infos,20,3) 
    try:
        # GET请求方式，get()获取指定Key值所对应的value值
        # 获取index的值，如果没有，则设置使用默认值1
        num = request.GET.get('index','1')
        # 获取第几页
        number = paginator.page(num)
    except PageNotAnInteger:
        # 如果输入的页码数不是整数，那么显示第一页数据
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)
    # 将当前页页码，以及当前页数据传递到index.html
    context={'page':number,'paginator':paginator,'form':form,'form1':form1,'form2':form2}
    return render(request, 'management/ot_list.html', context)

@login_required
def ot_search(request):
    form = OtForm(label_suffix='')
    form2 = OtForm1(label_suffix='')
    global name
    if request.method != "POST":
        form1 = OtSearchForm(label_suffix='')
        users =OvertimeInfo.objects.filter().order_by('-date')
    else:
        form1 = OtSearchForm(request.POST)
        if form1.is_valid():
            name=form1.cleaned_data['name']     
        else:
            print('不合理啊！')
    users =OvertimeInfo.objects.filter(name__contains=name).order_by('-date')
    paginator = Paginator(users,20,3) 
    try:
        num = request.GET.get('index','1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)
    context={'page':number,'paginator':paginator,'form1': form1,'form': form,'name':name,'form2': form2}
    return render(request, 'management/ot_list.html', context)

# 登记加班
@login_required
def add_ot(request):
    if request.method != "POST":
        form = OtForm(label_suffix='')
    else:
        form = OtForm(request.POST)
        if form.is_valid():
            ot = OvertimeInfo(date=request.POST.get('date'), 
                        work_type=request.POST.get('work_type'),
                        work_info = request.POST.get('work_info'),
                        name = request.POST.get('name'),
                        expense = request.POST.get('expense'),
                        extra=request.POST.get('extra'))
            ot.save()
            messages.success(request, "登记成功！")
            return HttpResponse('ok')     
        else:
            print('不合法的表单')
    return render(request, "management/ot_list.html",{'form': form})

#修改加班信息
@login_required
def ot_update(request):  
    edit_id =request.POST.get('id')
    print(edit_id)
    if request.method != "POST":
        form2 = OtForm1(label_suffix='')
    else:
        form2 = OtForm1(request.POST)
        if form2.is_valid():
            # OvertimeInfo1=OvertimeInfo.objects.filter(id=edit_id)
            ot = OvertimeInfo(id=request.POST.get('id'), 
                        date=request.POST.get('date'), 
                        work_type=request.POST.get('work_type'),
                        work_info = request.POST.get('work_info'),
                        name = request.POST.get('name'),
                        expense = request.POST.get('expense'),
                        extra=request.POST.get('extra'))

            ot.save()
            messages.success(request, "修改成功！")
            return HttpResponse('ok')
        else:
            print('表单不合法！')
    return render(request, "management/ot_list.html",{'form2': form2})

#批量操作
@login_required
def ot_batch(request):
    if 'delete_list' in request.POST:#删除
        ot_id=request.POST.getlist("d2p_list")
        ot_infos = OvertimeInfo.objects.filter(id__in=ot_id)
        for ot_info in ot_infos:
                ot_info.delete() 
        ot_infos = OvertimeInfo.objects.all()       
    return HttpResponseRedirect(reverse('management:ot_list'))

# 工作日志列表
@login_required
def worklog(request):
    global logs
    if request.method != "POST":
        form = WlForm(label_suffix='')
        form1 =WlSearchForm(label_suffix='')
        form2 = WlForm1(label_suffix='')
        form3 = UlForm(label_suffix='')
    else:
        form = WlForm(request.POST)
        if form.is_valid():
            wl = WorklogInfo(date=form.cleaned_data['date'], 
                        text=form.cleaned_data['text'],
                        user = request.user)
            wl.save()
            return HttpResponseRedirect(reverse('management:worklog'))
        else:
            print('不合法的表格')
    curr_user=str(request.user)
    # user_tmp=User.objects.values_list('username',flat=True).filter(is_superuser=0)
    logs=WorklogInfo.objects.filter(user=curr_user).order_by('-date')
    paginator = Paginator(logs,20,3) 
    try:
        num = request.GET.get('index','1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)
    context={'page':number,'paginator':paginator,'form':form,'form1':form1,'form2':form2,'form3':form3,'logs':logs}
    return render(request, 'management/worklog.html', context)

# 员工工作日志列表
# @login_required
# def worklog_subordinate(request):
#     global logs
#     if request.method != "POST":
#         form1 =WlSearchForm(label_suffix='')
#     # else:
#     #     form = WlForm(request.POST)
#     #     if form.is_valid():
#     #         wl = WorklogInfo(date=form.cleaned_data['date'], 
#     #                     text=form.cleaned_data['text'],
#     #                     user = request.user)
#     #         wl.save()
#     #         return HttpResponseRedirect(reverse('management:worklog'))
#     #     else:
#     #         print('不合法的表格')
#     curr_user=str(request.user)
#     logs=WorklogInfo.objects.filter(user__is_superuser__is=0).order_by('-date')
#     paginator = Paginator(logs,20,3) 
#     try:
#         num = request.GET.get('index','1')
#         number = paginator.page(num)
#     except PageNotAnInteger:
#         number = paginator.page(1)
#     except EmptyPage:
#         number = paginator.page(paginator.num_pages)
#     context={'page':number,'paginator':paginator,'form':form,'form1':form1,'logs':logs}
#     return render(request, 'management/worklog_subordinate.html', context)

#职级维护
# @login_required
# def add_level(request):
#     if request.method != "POST":
#         form = CrmForm(label_suffix='')
#     else:
#         form = CrmForm(request.POST)
#         if form.is_valid():
#             crm = CrmExamInfo(name=form.cleaned_data['name'], 
#                         user_code=form.cleaned_data['user_code'],
#                         exam_name = form.cleaned_data['exam_name'],
#                         time_limit = form.cleaned_data['time_limit'],
#                         times = form.cleaned_data['times'],
#                         real_times=form.cleaned_data['real_times'],
#                         point=form.cleaned_data['point'])
#             crm.save()
#             messages.success(request, "数据提交成功！")
#             return HttpResponseRedirect(reverse('data:list'))
            
#         else:
#             print('fuck2')
#     return render(request, "data/list.html",{'form': form})

# 新增日志
@login_required
def worklog_add(request):
    if request.method != "POST":
        form = WlForm(label_suffix='')
    else:
        form = WlForm(request.POST)
        if form.is_valid():
            ot = WorklogInfo(date=request.POST.get('date'), 
                        text=request.POST.get('text'),
                        user=request.user)
            ot.save()
            messages.success(request, "新增成功！")
            return HttpResponse('ok')     
        else:
            print('不合法的表单')
    return render(request, "management/worklog.html",{'form': form})

#修改工作日志
@login_required
def worklog_update(request):  
    edit_id =request.POST.get('id')
    print(edit_id)
    if request.method != "POST":
        form2 = WlForm1(label_suffix='')
    else:
        form2 = WlForm1(request.POST)
        if form2.is_valid():
            ot = WorklogInfo(id=request.POST.get('id'), 
                        date=request.POST.get('date'), 
                        text=request.POST.get('text'),
                        user=str(request.user))#因为user是系统默认的，且是bid.bidder类型，所以加上str

            ot.save()
            messages.success(request, "修改成功！")
            return HttpResponse('ok')
        else:
            print('表单不合法！')
    return render(request, "management/worklog.html",{'form2': form2})

#查询工作日志
@login_required
def worklog_search(request):
    form = WlForm(label_suffix='')
    form2 = WlForm1(label_suffix='')
    curr_user=str(request.user)
    global logs
    if request.method != "POST":
        form1 = WlSearchForm(label_suffix='')
        logs =WorklogInfo.objects.filter(user=curr_user).order_by('-date')
    else:
        form1 = WlSearchForm(request.POST)
        if form1.is_valid():
            today=time.strftime('%Y-%m-%d',time.localtime(time.time()))#取今日日期
            bg_date=form1.cleaned_data['bg_date'] 
            en_date=form1.cleaned_data['en_date']
            keyword=form1.cleaned_data['keyword']
            if en_date=='':#如果截止日期为空，则默认为当日日期
                en_date=today  
        else:
            print('表单不合法！')
    logs =WorklogInfo.objects.filter(date__range=[bg_date,en_date],text__contains=keyword,user=curr_user).order_by('-date') #起始日期为空，则小于截止日期都会显示
    paginator = Paginator(logs,20,3) 
    try:
        num = request.GET.get('index','1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)
    context={'page':number,'paginator':paginator,'form1': form1,'form': form,'form2': form2,'logs':logs}
    return render(request, 'management/worklog.html', context)

#删除日志
@login_required
def worklog_delete(request):
    delete_id=request.POST.get('id')
    if delete_id:
        log = WorklogInfo.objects.filter(id=delete_id)
        log.delete()
        messages.success(request, "删除成功！")
        return HttpResponse('ok')
    else:
        print('不存在的值')
    return render(request, "management/worklog.html")

#导出日志
@login_required
def worklog_export(request):
    column_names = ["id","date","text","user"]
    return django_excel.make_response_from_query_sets(logs,column_names[1:3], "xlsx",status = 200 ,sheet_name='测试',file_name='测试文件')
    print("导出成功！")
