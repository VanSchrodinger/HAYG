from django.shortcuts import render
from django.http import HttpResponseRedirect,FileResponse,HttpResponse
from django.template import RequestContext
from django.urls import reverse
from django.utils.http import urlquote
from .models import CrmExamInfo,ScanInfo
from django.db.models import Q
from .forms import UploadForm,FolderForm,CrmForm,CrmSearchForm,ShineSearchForm
import os,stat,shutil,sys,win32com.client
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import get_user
import pythoncom
from pydocx import PyDocX
from PyPDF2 import PdfFileReader, PdfFileWriter
import time,xlrd,pymysql
from django.contrib import messages
import pandas as pd
from sqlalchemy import create_engine
from tkinter import messagebox
import json


# 上传考试成绩
@login_required
def input(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file')
            for f in files:
                file_path=os.path.join('Z:\\PYTHON_FILE\\CRM', f.name)
                destination = open(file_path, 'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
                book = xlrd.open_workbook(file_path)
                sheet = book.sheet_by_name("Sheet0")   #execl里面的worksheet1
                row_num = sheet.nrows
                for i in range(1, row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
                    row_data = sheet.row_values(i)
                    examinfo=CrmExamInfo(name=row_data[0],
                        user_code =row_data[1] ,
                        exam_name =row_data[2] ,
                        time_limit =row_data[3], 
                        times =row_data[4], 
                        real_times=row_data[5], 
                        point=row_data[6] )
                    examinfo.save()
            # 返回上传页
            return HttpResponseRedirect(reverse('data:list'))
    else:
        form = UploadForm()  # A empty, unbound form
    return render(request, 'data/input.html', {'form': form})

# 成绩首页
@login_required
def list(request):
    if request.method != "POST":
        form = CrmForm(label_suffix='')
        form1 =CrmSearchForm(label_suffix='')
        print('现在是get网页')
    else:
        form = CrmForm(request.POST)
        if form.is_valid():
            crm = CrmExamInfo(name=form.cleaned_data['name'], 
                        user_code=form.cleaned_data['user_code'],
                        exam_name = form.cleaned_data['exam_name'],
                        time_limit = form.cleaned_data['time_limit'],
                        times = form.cleaned_data['times'],
                        real_times=form.cleaned_data['real_times'],
                        point=form.cleaned_data['point'])
            crm.save()
            return HttpResponseRedirect(reverse('data:list'))
        else:
            print('fuck2')

    crm_infos=CrmExamInfo.objects.filter().order_by('-create_date')
    # file_floders=Topic.objects   
    paginator = Paginator(crm_infos,20,3) 
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
    context={'page':number,'paginator':paginator,'form':form,'form1':form1}
    return render(request, 'data/list.html', context)
@login_required
def crmsearch(request):
    form = CrmForm(label_suffix='')
    global name
    if request.method != "POST":
        form1 = CrmSearchForm(label_suffix='')
        users =CrmExamInfo.objects.filter().order_by('-create_date')
    else:
        form1 = CrmSearchForm(request.POST)
        if form1.is_valid():
            name=form1.cleaned_data['name']     
        else:
            print('不合理啊！')
    users =CrmExamInfo.objects.filter(name__contains=name).order_by('-create_date')
    paginator = Paginator(users,20,3) 
    try:
        num = request.GET.get('index','1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)
    context={'page':number,'paginator':paginator,'form1': form1,'form': form,'name':name}
    return render(request, 'data/list.html', context)

#单个新增成绩
@login_required
def add_crm(request):
    if request.method != "POST":
        form = CrmForm(label_suffix='')
    else:
        form = CrmForm(request.POST)
        if form.is_valid():
            crm = CrmExamInfo(name=form.cleaned_data['name'], 
                        user_code=form.cleaned_data['user_code'],
                        exam_name = form.cleaned_data['exam_name'],
                        time_limit = form.cleaned_data['time_limit'],
                        times = form.cleaned_data['times'],
                        real_times=form.cleaned_data['real_times'],
                        point=form.cleaned_data['point'])
            crm.save()
            messages.success(request, "数据提交成功！")
            return HttpResponseRedirect(reverse('data:list'))
            
        else:
            print('fuck2')
    return render(request, "data/list.html",{'form': form})

#批量操作
@login_required
def batch(request):
    if 'delete_list' in request.POST:# 删主文件夹
        if 'delete_list' in request.POST:
            crm_id=request.POST.getlist("d2p_list")
            crm_infos = CrmExamInfo.objects.filter(id__in=crm_id)
            for crm_info in crm_infos:
                    crm_info.delete() 
            crm_infos = CrmExamInfo.objects.all()
    return HttpResponseRedirect(reverse('data:list'))

# 无纸化率首页
@login_required
def shine(request):
    if request.method != "POST":
        form = CrmForm(label_suffix='')
        form1 =ShineSearchForm(label_suffix='')
        form2 = UploadForm(request.POST, request.FILES)
    else:
        form = CrmForm(request.POST)
        form2 = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            crm = CrmExamInfo(name=form.cleaned_data['name'], 
                        user_code=form.cleaned_data['user_code'],
                        exam_name = form.cleaned_data['exam_name'],
                        time_limit = form.cleaned_data['time_limit'],
                        times = form.cleaned_data['times'],
                        real_times=form.cleaned_data['real_times'],
                        point=form.cleaned_data['point'])
            crm.save()
            return HttpResponseRedirect(reverse('data:list'))
        else:
            print('fuck2')
    scan_infos=ScanInfo.objects.filter().order_by('-id')
    paginator = Paginator(scan_infos,20,3) 
    try:
        num = request.GET.get('index','1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)
    context={'page':number,'paginator':paginator,'form':form,'form1':form1,'form2':form2}
    return render(request, 'data/shine.html', context)

# 上传无纸化后台数据
@login_required
def input_shine(request):
    if request.method == 'POST':
        form2 = UploadForm(request.POST, request.FILES)
        if form2.is_valid():
            files = request.FILES.getlist('file')
            for f in files:
                file_path=os.path.join('Z:\\PYTHON_FILE\\SHINE', f.name)
                destination = open(file_path, 'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
                df =pd.read_csv(file_path,encoding="gbk")
                df.index.name = 'id'
                engine = create_engine("mysql+mysqlconnector://root:password@127.0.0.1:3306/jzyy",echo=False)
                df.to_sql(name = 'data_scaninfo',con = engine,if_exists="append")
                messages.success(request, "数据提交成功！")
            return HttpResponseRedirect(reverse('data:shine'))
    else:
        form2 = UploadForm()  
    return render(request, 'data/shine.html', {'form2': form2})

@login_required
def shinesearch(request):
    form = CrmForm(label_suffix='')
    form2 = UploadForm(request.POST, request.FILES)
    global source_name,busi_name,app_id,is_ecimc        
    if request.method != "POST":
        form1 = ShineSearchForm(label_suffix='')
        users =ScanInfo.objects.filter().order_by('-id')
    else:
        form1 = ShineSearchForm(request.POST)
        if form1.is_valid():
            source_name=form1.cleaned_data['source_name']
            busi_name=form1.cleaned_data['busi_name']
            app_id=form1.cleaned_data['app_id']
            is_ecimc=form1.cleaned_data['is_ecimc']      
        else:
            print('不合理啊！')
    users =ScanInfo.objects.filter(source_name__contains=source_name,busi_name__contains=busi_name,app_id__contains=app_id,is_ecimc__contains=is_ecimc).order_by('-id')
    paginator = Paginator(users,20,3) 
    try:
        num = request.GET.get('index','1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)
    context={'page':number,'paginator':paginator,'form1': form1,'form': form,'form2': form2,'is_ecimc':is_ecimc,'source_name':source_name,'busi_name':busi_name,'app_id':app_id}
    return render(request, 'data/shine.html', context)


