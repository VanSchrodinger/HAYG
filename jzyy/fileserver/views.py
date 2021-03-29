
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.http import FileResponse
from django.template import RequestContext
from django.urls import reverse
from django.utils.http import urlquote
from .models import FileInfo,Xqtj
from jzyy_notes.models import Topic
from django.db.models import Q
from django.db import connection
from .forms import UploadForm,FolderForm,FileForm
import os,stat,shutil,sys,win32com.client
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import get_user
import pythoncom
from pydocx import PyDocX
from PyPDF2 import PdfFileReader, PdfFileWriter
import time,xlrd,pymysql
from django.contrib import messages
import datetime
#pdf-word
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


#根目录

#上传-文件(公共、个人)
@login_required
def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file')
            for f in files:
                if B=='0':
                    file_info = FileInfo(file_name=f.name, 
                        file_size=1 if 0 < f.size < 1024 else f.size / 1024, 
                        file_path=os.path.join('E:\\PYTHON_FILE', f.name),
                        file_type=f.name.split('.')[-1],
                        load_user=get_user(request),
                        is_personal=int(B),
                        folder_name=os.path.join('E:\\PYTHON_FILE', f.name).split(f.name)[0])                   
                    file_info.save()
                    # 上传
                    destination = open(os.path.join("E:\\PYTHON_FILE", f.name), 'wb+')
                    for chunk in f.chunks():
                        destination.write(chunk)
                    destination.close()
                else:
                    file_info = FileInfo(file_name=f.name, 
                        file_size=1 if 0 < f.size < 1024 else f.size / 1024, 
                        file_path=os.path.join('E:\\PYTHON_FILE', str(get_user(request))+'\\'+f.name),
                        file_type=f.name.split('.')[-1],
                        load_user=get_user(request),
                        is_personal=int(B),
                        folder_name='E:\\PYTHON_FILE\\'+str(get_user(request)))                   
                    file_info.save()
                    # 上传
                    destination = open(os.path.join("E:\\PYTHON_FILE", str(get_user(request))+'\\'+f.name), 'wb+')
                    for chunk in f.chunks():
                        destination.write(chunk)
                    destination.close()
            # 返回上传页
            messages.success(request, "文件上传成功！")
            return HttpResponseRedirect(reverse('fileserver:list',args=[B]))
    else:
        form = UploadForm()  # A empty, unbound form
    return render(request, 'fileserver/upload.html', {'form': form})

#新增-文件夹(公共，个人)
@login_required
def new_folder(request):
    # 添加新主题
    if request.method !='POST':
        form3=FolderForm()
    else:
        form3=FolderForm(request.POST)
        if form3.is_valid():
            folder_name=form3.cleaned_data['folder']
            if B=='0':
                file_info = FileInfo(file_name=folder_name, 
                        file_size=0, 
                        file_path=os.path.join('E:\\PYTHON_FILE', folder_name),
                        file_type='FOLDER',
                        load_user=get_user(request),
                        is_personal=int(B),
                        folder_name='E:\\PYTHON_FILE')                
                file_info.save()
                x=os.path.join("E:\\PYTHON_FILE", folder_name)
            else:
                file_info = FileInfo(file_name=folder_name, 
                        file_size=0, 
                        file_path=os.path.join('E:\\PYTHON_FILE', str(get_user(request))+'\\'+folder_name),
                        file_type='FOLDER',
                        load_user=get_user(request),
                        is_personal=int(B),
                        folder_name='E:\\PYTHON_FILE\\'+str(get_user(request)))                
                file_info.save()
                x=os.path.join('E:\\PYTHON_FILE', str(get_user(request))+'\\'+folder_name)
                z='E:\\PYTHON_FILE\\'+str(get_user(request))
                if not os.path.exists(z):
                    os.makedirs(z)
            os.mkdir(x)
            messages.success(request, "文件夹创建成功！")
            return HttpResponseRedirect(reverse('fileserver:list',args=[B]))
    context={'form3':form3} 
    return render(request,'fileserver/new_folder.html',context)

# 文件列表(公共，个人)
@login_required
def list(request,p):
    global B
    B=p
    form = UploadForm(request.POST, request.FILES)
    form3=FolderForm(request.POST)
    form_file=FileForm()
    if p=='0':
        sql = "SELECT * FROM jzyy.fileserver_fileinfo where is_personal=0 and folder_name=%s order by upload_time desc   "
        file_infos=FileInfo.objects.raw(sql,['E:\\PYTHON_FILE'])
        # file_infos=FileInfo.objects.filter(is_personal=0,folder_name='E:\\PYTHON_FILE\\').order_by('-upload_time')
    elif p=='2':
        file_infos=FileInfo.objects.filter(is_personal=2,folder_name='E:\\PYTHON_FILE').order_by('-upload_time')
    else:
        now_user=get_user(request)
        file_infos=FileInfo.objects.filter(load_user=now_user,is_personal=1,folder_name='E:\\PYTHON_FILE\\'+str(now_user)).order_by('-upload_time')
        # file_floders=Topic.objects   
    paginator = Paginator(file_infos,20,3) 
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
    context={'page':number,'paginator':paginator,'form':form,'form3':form3,'form_file':form_file}
    return render(request, 'fileserver/list.html', context)
# 移动文件
@login_required
def move_list(request,p):
    global B
    B=p
    form = UploadForm(request.POST, request.FILES)
    form3=FolderForm(request.POST)
    form_file=FileForm()
    if p=='0':
        sql = "SELECT * FROM jzyy.fileserver_fileinfo where is_personal=0 and folder_name=%s order by upload_time desc   "
        file_infos=FileInfo.objects.raw(sql,['E:\\PYTHON_FILE'])
        # file_infos=FileInfo.objects.filter(is_personal=0,folder_name='E:\\PYTHON_FILE\\').order_by('-upload_time')
    elif p=='2':
        file_infos=FileInfo.objects.filter(is_personal=2,folder_name='E:\\PYTHON_FILE').order_by('-upload_time')
    else:
        now_user=get_user(request)
        file_infos=FileInfo.objects.filter(load_user=now_user,is_personal=1,folder_name='E:\\PYTHON_FILE\\'+str(now_user)).order_by('-upload_time')
        # file_floders=Topic.objects   
    paginator = Paginator(file_infos,20,3) 
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
    context={'page':number,'paginator':paginator,'form':form,'form3':form3,'form_file':form_file}
    return render(request, 'fileserver/move_list.html', context)

#子目录

# 上传-文件
@login_required
def upload1(request):
    fp = a
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file')
            for f in files:
                file_info = FileInfo(file_name=f.name, 
                    file_size=1 if 0 < f.size < 1024 else f.size / 1024, 
                    file_path=os.path.join(fp, f.name),
                    file_type=f.name.split('.')[-1],
                    load_user=get_user(request),
                    is_personal=int(B),
                    folder_name=fp)                   
                file_info.save()
                destination = open(os.path.join(fp, f.name), 'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
            messages.success(request, "文件上传成功！")
            return HttpResponseRedirect(reverse('fileserver:list1',args=[a]))
    else:
        form = UploadForm()  # A empty, unbound form   
    return render(request, 'fileserver/upload1.html', {'form': form})


#新增-文件夹
@login_required
def new_folder1(request):
    fp = a
    form = UploadForm(request.POST, request.FILES)
    if request.method !='POST':
        form3=FolderForm()
    else:
        form3=FolderForm(request.POST)
        if form3.is_valid():
            folder_name=form3.cleaned_data['folder']
            file_info = FileInfo(file_name=folder_name, 
                    file_size=0, 
                    file_path=os.path.join(fp, folder_name),
                    file_type='FOLDER',
                    load_user=get_user(request),
                    is_personal=int(B),
                    folder_name=fp)                  
            file_info.save()
            x=os.path.join(fp, folder_name)
            os.mkdir(x)
            messages.success(request, "文件夹创建成功！")
            return HttpResponseRedirect(reverse('fileserver:list1',args=[a]))
    context={'form3':form3} 
    return render(request,'fileserver/new_folder1.html',context)

# 文件列表
@login_required
def list1(request,foler_name1):
    global a
    a=foler_name1
    contents =a.split('\\')[2:]
    i =0
    contents2 =[]
    contents_len=len(contents)
    while i<contents_len:
        if i==0:
            contents2.append('\\'+contents[i])
        else:
            contents2.append(contents2[i-1]+'\\'+contents[i])
        i=i+1
    contents3 = dict(zip(contents, contents2))
    allcontents='E:\\PYTHON_FILE'
    form = UploadForm(request.POST, request.FILES)
    form3=FolderForm(request.POST)
    form_file=FileForm()
    if B=='0':
        file_infos=FileInfo.objects.filter(is_personal=0,folder_name=a).order_by('-upload_time')
    elif B=='2':
        file_infos=FileInfo.objects.filter(is_personal=2,folder_name=a).order_by('-upload_time')    
    else:
        now_user=get_user(request)
        file_infos=FileInfo.objects.filter(folder_name=a,load_user=now_user,is_personal=1).order_by('-upload_time')        
    # file_floders=Topic.objects   
    paginator = Paginator(file_infos,20,3) 
    try:
        num = request.GET.get('index','1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)
    context={'page':number,'paginator':paginator,'form':form,'form3':form3,'form_file':form_file,'contents3':contents3,'allcontents':allcontents}
    return render(request, 'fileserver/list1.html', context)   
    
# 重命名
@login_required
def edit_filename(request):
    form = UploadForm(request.POST, request.FILES)
    form3=FolderForm(request.POST)
    file_id =request.POST.get('id')
    rnfile=FileInfo.objects.get(id=file_id)
    if request.method !='POST':
        form_file=FileForm(instance=rnfile,label_suffix='')
    else:
        form_file=FileForm(request.POST)
        file_path1=request.POST.get('folder_name')
        file_path2=file_path1+'\\'+request.POST.get('file_name')#新路径
        dict1=FileInfo.objects.filter(id=request.POST.get('id')).values('file_path')
        file_path3=dict1[0].get('file_path')#原路径
        FileInfo.objects.filter(id=request.POST.get('id')).update(file_name=request.POST.get('file_name'),upload_time=datetime.datetime.now(),file_path=file_path2) 
        #文件夹的情况
        # folder_name1=FileInfo.objects.filter(folder_name__contains=file_path3).values('folder_name')
        # folder_name2=folder_name1.get('folder_name').replace(file_path3,file_path2)
        # FileInfo.objects.filter(folder_name__contains=file_path3).update(folder_name=folder_name2)
        with connection.cursor() as cursor: 
            cursor.execute("update jzyy.fileserver_fileinfo  set  folder_name = replace(folder_name,%s,%s),file_path = replace(file_path,%s,%s) where folder_name like concat('%%',%s,'%%');",[file_path3,file_path2,file_path3,file_path2,file_path3.replace('\\','\\\\')])
        # sql="update jzyy.fileserver_fileinfo  set  folder_name = replace(folder_name,'%s','%s') where folder_name like concat('%%','%s','%%')"
        # FileInfo.objects.raw(sql,params=[file_path3.replace('\\','\\\\'),file_path2.replace('\\','\\\\'),file_path3.replace('\\','\\\\\\\\')])
        # print(str(FileInfo.objects.raw(sql,params=[file_path3.replace('\\','\\\\'),file_path2.replace('\\','\\\\'),file_path3.replace('\\','\\\\\\\\')]).query))
        os.rename(file_path3,file_path2)        
        return HttpResponse('ok')
    context={'form3':form3,'form':form,'form_file':form_file}
    return render(request,'jzyy_notes/edit_topic.html',context)
# 功能区
    # 下载文件
@login_required
def download(request, id):
    file_info = FileInfo.objects.get(id=id)
    print('下载的文件名：' + file_info.file_name)
    file = open(file_info.file_path, 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(file_info.file_name)
    return response

    #删除包含文件的文件夹
def delete_all(rootdir):
    for dir_path,subpaths,files in os.walk(rootdir,False):
        for file in files:
            file_path=os.path.join(dir_path,file)
            os.remove(file_path)
        os.rmdir(dir_path)                 

    # 删除子文件夹-文件
@login_required
def delete_son(request, file_id):
    file_info = FileInfo.objects.get(id=file_id)
    if file_info.file_type == 'FOLDER':
        delete_all(file_info.file_path)
        d_f=file_info.file_path
        file_info1=FileInfo.objects.filter(folder_name__contains=d_f)
        file_info1.delete()
        file_info.delete() 
    else:
        os.remove(file_info.file_path)
        file_info.delete() 
    file_infos = FileInfo.objects.all()
    
    return HttpResponseRedirect(reverse('fileserver:list1',args=[a]))

    # 删除子文件夹-文件
@login_required
def son_delete(request):
    file_id=request.POST.get('id')
    file_info = FileInfo.objects.get(id=file_id)
    if file_info.file_type == 'FOLDER':
        delete_all(file_info.file_path)
        d_f=file_info.file_path
        file_info1=FileInfo.objects.filter(folder_name__contains=d_f)
        file_info1.delete()
        file_info.delete() 
    else:
        os.remove(file_info.file_path)
        file_info.delete() 
    return HttpResponse('ok') 
    file_infos = FileInfo.objects.all()

    return HttpResponseRedirect(reverse('fileserver:list1',args=[a]))

    # 删主文件夹-文件
@login_required
def delete(request, file_id):
    file_info = FileInfo.objects.get(id=file_id)
    if file_info.file_type == 'FOLDER':
        delete_all(file_info.file_path)
        d_f=file_info.file_path
        file_info1=FileInfo.objects.filter(folder_name__contains=d_f)
        file_info1.delete()
        file_info.delete() 
    else:
        os.remove(file_info.file_path)
        file_info.delete() 
    file_infos = FileInfo.objects.all()
    
    return HttpResponseRedirect(reverse('fileserver:list',args=[B]))
    #删主文件夹-文件
@login_required
def file_delete(request):
    file_id=request.POST.get('id')
    file_info = FileInfo.objects.get(id=file_id)
    if file_info.file_type == 'FOLDER':
        delete_all(file_info.file_path)
        d_f=file_info.file_path
        file_info1=FileInfo.objects.filter(folder_name__contains=d_f)
        file_info1.delete()
        file_info.delete()
    else:
        os.remove(file_info.file_path)
        file_info.delete()
    messages.success(request, "删除成功！")
    return HttpResponse('ok') 
    file_infos = FileInfo.objects.all()
    
    return HttpResponseRedirect(reverse('fileserver:list',args=[B]))


    #文件模块返回上一级
def return_file(request):
    locate=a.rfind('\\')
    return_name=a[:locate+1]
    if return_name=='E:\\PYTHON_FILE\\':
        return HttpResponseRedirect(reverse('fileserver:list',args=[B]))
    else:
        return_name1=a[:locate]
        return HttpResponseRedirect(reverse('fileserver:list1',args=[return_name1]))

    #DOC转换PDF功能
@login_required
def d2p(request, file_id):
    pythoncom.CoInitialize()
    file_info = FileInfo.objects.get(id=file_id)
    in_file=file_info.file_path
    out_file=file_info.file_path.split(".")[0]+".pdf"
    word = win32com.client.Dispatch('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=17)
    doc.Close()
    # word.Quit()
    file_info1 = FileInfo(file_name=file_info.file_name.split('.')[0]+'.pdf', 
                    file_path=out_file,
                    file_type='pdf',
                    load_user=get_user(request),
                    is_personal=int(B),
                    folder_name=file_info.folder_name)                  
    file_info1.save()
    file_size1=os.path.getsize(out_file)
    FileInfo.objects.filter(file_path=out_file).update(file_size=1 if 0 < file_size1 < 1024 else file_size1 / 1024)
    
    return HttpResponseRedirect(reverse('fileserver:list',args=[B]))

    #批量控制台-主文件夹
@login_required
def postlist(request):
    if 'delete_list' in request.POST:# 删主文件夹
        if 'delete_list' in request.POST:
            pdf_id=request.POST.getlist("d2p_list")
            file_infos = FileInfo.objects.filter(id__in=pdf_id)
            for file_info in file_infos:
                if file_info.file_type == 'FOLDER':
                    delete_all(file_info.file_path)
                    file_info.delete()
                else:
                    os.remove(file_info.file_path)
                    file_info.delete() 
            file_infos = FileInfo.objects.all()
        messages.success(request, "文件删除成功！")
    elif   'mpdf_list' in request.POST:#合并PDF
        output = PdfFileWriter()
        outputPages = 0
        output_name=''
        pdf_id=request.POST.getlist("d2p_list")
        file_infos = FileInfo.objects.filter(id__in=pdf_id)
        for file_info in file_infos:
            # 读取源PDF文件
            input = PdfFileReader(open(file_info.file_path, "rb"))

            # 获得源PDF文件中页面总数
            pageCount = input.getNumPages()
            outputPages += pageCount
            print("页数：%d"%pageCount)

            # 分别将page添加到输出output中
            for iPage in range(pageCount):
                output.addPage(input.getPage(iPage))
            # output_name=output_name+file_info.file_name.split('.')[0][0]+'-'
        output_name = '整合-' + file_info.folder_name.split('\\')[-1]

        # 写入到目标PDF文件
        outputStream = open(file_infos[0].folder_name+'\\'+ output_name+'.pdf', "wb")
        output.write(outputStream)
        outputStream.close()
        file_info1 = FileInfo(file_name=output_name+'.pdf', 
                    file_path=file_infos[0].folder_name+'\\'+output_name+'.pdf',
                    file_type='pdf',
                    load_user=get_user(request),
                    is_personal=int(B),
                    folder_name=file_infos[0].folder_name)                  
        file_info1.save()
        file_size1=os.path.getsize(file_infos[0].folder_name+'\\'+output_name+'.pdf')
        FileInfo.objects.filter(file_path=file_infos[0].folder_name+'\\'+output_name+'.pdf').update(file_size=1 if 0 < file_size1 < 1024 else file_size1 / 1024)
        messages.success(request, "PDF合并成功！")
    elif 'download_list' in request.POST:# 下载
        download_id=request.POST.getlist("d2p_list")
        file_infos = FileInfo.objects.filter(id__in=download_id)
        # print('下载的文件名：' + file_info.file_name)
        for file_info in file_infos:
            file = open(file_info.file_path, 'rb')
            response = FileResponse(file)
            response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(file_info.file_name)
            return response
    elif 'tj_list'in request.POST:#转换成WORD
        word_id=request.POST.getlist("d2p_list")
        file_infos = FileInfo.objects.filter(id__in=word_id)
        for file_info in file_infos:
            in_file=file_info.file_path
            out_file=file_info.file_path.split(".")[0]+".doc"
            fp = open(in_file, 'rb')  # 以二进制读模式打开
            # 用文件对象来创建一个pdf文档分析器
            parser = PDFParser(fp)
            # 创建一个PDF文档
            doc = PDFDocument()
            # 连接分析器 与文档对象
            parser.set_document(doc)
            doc.set_parser(parser)
            # 提供初始化密码
            # 如果没有密码 就创建一个空的字符串
            doc.initialize()
            if not doc.is_extractable:
                raise PDFTextExtractionNotAllowed
            else:
                # 创建PDf 资源管理器 来管理共享资源
                rsrcmgr = PDFResourceManager()
                # 创建一个PDF设备对象
                laparams = LAParams()
                device = PDFPageAggregator(rsrcmgr, laparams=laparams)
                # 创建一个PDF解释器对象
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                # 用来计数页面，图片，曲线，figure，水平文本框等对象的数量
                num_page, num_image, num_curve, num_figure, num_TextBoxHorizontal = 0, 0, 0, 0, 0
                for page in doc.get_pages(): # doc.get_pages() 获取page列表
                    num_page += 1  # 页面增一
                    interpreter.process_page(page)
                    # 接受该页面的LTPage对象
                    layout = device.get_result()
                    for x in layout:
                        if isinstance(x,LTImage):  # 图片对象
                            num_image += 1
                        if isinstance(x,LTCurve):  # 曲线对象
                            num_curve += 1
                        if isinstance(x,LTFigure):  # figure对象
                            num_figure += 1
                        if isinstance(x, LTTextBoxHorizontal):  # 获取文本内容
                            num_TextBoxHorizontal += 1  # 水平文本框对象增一
                            # 保存文本内容
                            with open(out_file, 'a',encoding='utf-8') as f:    #生成doc文件的文件名及路径
                                results = x.get_text()
                                f.write(results)
                                f.write('\n')
                print('对象数量：\n','页面数：%s\n'%num_page,'图片数：%s\n'%num_image,'曲线数：%s\n'%num_curve,'水平文本框：%s\n'
                    %num_TextBoxHorizontal)
                file_info1 = FileInfo(file_name=file_info.file_name.split('.')[0]+'.doc', 
                            file_path=out_file,
                            file_type='doc',
                            load_user=get_user(request),
                            is_personal=int(B),
                            folder_name=file_info.folder_name)                  
                file_info1.save()
                file_size1=os.path.getsize(out_file)
                FileInfo.objects.filter(file_path=out_file).update(file_size=1 if 0 < file_size1 < 1024 else file_size1 / 1024)
        messages.success(request, "DOC转换成功！")
    else:                             #转换成PDF
        pdf_id=request.POST.getlist("d2p_list")
        file_infos = FileInfo.objects.filter(id__in=pdf_id)
        for file_info in file_infos:
            in_file=file_info.file_path
            out_file=file_info.file_path.split(".")[0]+".pdf"
            pythoncom.CoInitialize()
            if file_info.file_type in ('doc','docx'):
                word = win32com.client.Dispatch('Word.Application')
            elif file_info.file_type in ('xls','xlsx'):
                word = win32com.client.Dispatch('Excel.Application')
            elif file_info.file_type in ('ppt','pptx'):
                word = win32com.client.Dispatch('PowerPoint.Application')
            doc = word.Documents.Open(in_file)
            doc.SaveAs(out_file, FileFormat=17)
            doc.Close()
            time.sleep(1)
            file_info1 = FileInfo(file_name=file_info.file_name.split('.')[0]+'.pdf', 
                        file_path=out_file,
                        file_type='pdf',
                        load_user=get_user(request),
                        is_personal=int(B),
                        folder_name=file_info.folder_name)                  
            file_info1.save()
            file_size1=os.path.getsize(out_file)
            FileInfo.objects.filter(file_path=out_file).update(file_size=1 if 0 < file_size1 < 1024 else file_size1 / 1024)
        messages.success(request, "PDF合并成功！")
    return HttpResponseRedirect(reverse('fileserver:list',args=[B]))

    #批量控制台-子文件夹
@login_required
def postlist_son(request):
    if 'delete_list' in request.POST:# 删子文件夹-批量
        pdf_id=request.POST.getlist("d2p_list")
        file_infos = FileInfo.objects.filter(id__in=pdf_id)
        for file_info in file_infos:
            if file_info.file_type == 'FOLDER':
                delete_all(file_info.file_path)
                file_info.delete()
            else:
                os.remove(file_info.file_path)
                file_info.delete() 
        file_infos = FileInfo.objects.all()
        messages.success(request, "文件删除成功！")
    elif   'mpdf_list' in request.POST:# 合并PDF文件夹-批量
        output = PdfFileWriter()
        outputPages = 0
        output_name=''
        pdf_id=request.POST.getlist("d2p_list")
        file_infos = FileInfo.objects.filter(id__in=pdf_id)
        for file_info in file_infos:
            # 读取源PDF文件
            input = PdfFileReader(open(file_info.file_path, "rb"))

            # 获得源PDF文件中页面总数
            pageCount = input.getNumPages()
            outputPages += pageCount
            print("页数：%d"%pageCount)

            # 分别将page添加到输出output中
            for iPage in range(pageCount):
                output.addPage(input.getPage(iPage))
            # output_name=output_name+file_info.file_name.split('.')[0][0]+'-'
        output_name = '整合-' + file_info.folder_name.split('\\')[-1]

        # 写入到目标PDF文件
        outputStream = open(file_infos[0].folder_name+'\\'+ output_name+'.pdf', "wb")
        output.write(outputStream)
        outputStream.close()
        file_info1 = FileInfo(file_name=output_name+'.pdf', 
                    file_path=file_infos[0].folder_name+'\\'+output_name+'.pdf',
                    file_type='pdf',
                    load_user=get_user(request),
                    is_personal=int(B),
                    folder_name=file_infos[0].folder_name)                  
        file_info1.save()
        file_size1=os.path.getsize(file_infos[0].folder_name+'\\'+output_name+'.pdf')
        FileInfo.objects.filter(file_path=file_infos[0].folder_name+'\\'+output_name+'.pdf').update(file_size=1 if 0 < file_size1 < 1024 else file_size1 / 1024)
        messages.success(request, "PDF合并成功！")
    elif 'download_list' in request.POST:# 下载-子文件夹-批量
        download_id=request.POST.getlist("d2p_list")
        file_infos = FileInfo.objects.filter(id__in=download_id)
        # print('下载的文件名：' + file_info.file_name)
        for file_info in file_infos:
            file = open(file_info.file_path, 'rb')
            response = FileResponse(file)
            response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(file_info.file_name)
            return response
    elif 'tj_list'in request.POST:
        word_id=request.POST.getlist("d2p_list")
        file_infos = FileInfo.objects.filter(id__in=word_id)
        for file_info in file_infos:
            in_file=file_info.file_path
            out_file=file_info.file_path.split(".")[0]+".doc"
            fp = open(in_file, 'rb')  # 以二进制读模式打开
            # 用文件对象来创建一个pdf文档分析器
            parser = PDFParser(fp)
            # 创建一个PDF文档
            doc = PDFDocument()
            # 连接分析器 与文档对象
            parser.set_document(doc)
            doc.set_parser(parser)
            # 提供初始化密码
            # 如果没有密码 就创建一个空的字符串
            doc.initialize()
            if not doc.is_extractable:
                raise PDFTextExtractionNotAllowed
            else:
                # 创建PDf 资源管理器 来管理共享资源
                rsrcmgr = PDFResourceManager()
                # 创建一个PDF设备对象
                laparams = LAParams()
                device = PDFPageAggregator(rsrcmgr, laparams=laparams)
                # 创建一个PDF解释器对象
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                # 用来计数页面，图片，曲线，figure，水平文本框等对象的数量
                num_page, num_image, num_curve, num_figure, num_TextBoxHorizontal = 0, 0, 0, 0, 0
                for page in doc.get_pages(): # doc.get_pages() 获取page列表
                    num_page += 1  # 页面增一
                    interpreter.process_page(page)
                    # 接受该页面的LTPage对象
                    layout = device.get_result()
                    for x in layout:
                        if isinstance(x,LTImage):  # 图片对象
                            num_image += 1
                        if isinstance(x,LTCurve):  # 曲线对象
                            num_curve += 1
                        if isinstance(x,LTFigure):  # figure对象
                            num_figure += 1
                        if isinstance(x, LTTextBoxHorizontal):  # 获取文本内容
                            num_TextBoxHorizontal += 1  # 水平文本框对象增一
                            # 保存文本内容
                            with open(out_file, 'a',encoding='utf-8') as f:    #生成doc文件的文件名及路径
                                results = x.get_text()
                                f.write(results)
                                f.write('\n')
                print('对象数量：\n','页面数：%s\n'%num_page,'图片数：%s\n'%num_image,'曲线数：%s\n'%num_curve,'水平文本框：%s\n'
                    %num_TextBoxHorizontal)
                file_info1 = FileInfo(file_name=file_info.file_name.split('.')[0]+'.doc', 
                            file_path=out_file,
                            file_type='doc',
                            load_user=get_user(request),
                            is_personal=int(B),
                            folder_name=file_info.folder_name)                  
                file_info1.save()
                file_size1=os.path.getsize(out_file)
                FileInfo.objects.filter(file_path=out_file).update(file_size=1 if 0 < file_size1 < 1024 else file_size1 / 1024)
        messages.success(request, "DOC转换成功！")
    else:
        pdf_id=request.POST.getlist("d2p_list")
        file_infos = FileInfo.objects.filter(id__in=pdf_id)
        for file_info in file_infos:
            in_file=file_info.file_path
            out_file=file_info.file_path.split(".")[0]+".pdf"
            pythoncom.CoInitialize()
            word = win32com.client.Dispatch('Word.Application')
            doc = word.Documents.Open(in_file)
            doc.SaveAs(out_file, FileFormat=17)
            doc.Close()
            time.sleep(1)
            file_info1 = FileInfo(file_name=file_info.file_name.split('.')[0]+'.pdf', 
                        file_path=out_file,
                        file_type='pdf',
                        load_user=get_user(request),
                        is_personal=int(B),
                        folder_name=file_info.folder_name)                  
            file_info1.save()
            file_size1=os.path.getsize(out_file)
            FileInfo.objects.filter(file_path=out_file).update(file_size=1 if 0 < file_size1 < 1024 else file_size1 / 1024)
        messages.success(request, "PDF转换成功！")
    return HttpResponseRedirect(reverse('fileserver:list1',args=[a]))









#根据数据库内容渲染模板
def post(request,file_id):
    base_url = 'D:\\python\\jzyy\\tmp\\'
    asset_url = base_url + '华安证券集中运营模块内部审批单.docx'
    tpl = DocxTemplate(asset_url)
    file_info = FileInfo.objects.get(id=file_id)
    context = {'text': file_info.file_name}
    tpl.render(context)
    tpl.save(base_url + file_info.file_name +'.docx')
    return HttpResponseRedirect(reverse('fileserver:list1',args=[a]))

#在线预览docx
def docx_ol(request,file_id):
    file_info = FileInfo.objects.get(id=file_id)
    init_path= file_info.file_path
    html_path=file_info.file_path.split('.')[0]+'.html'
    html_name=file_info.file_name.split('.')[0]+'.html'
    # if file_info.file_type =='doc':
    #     doc2x(file_info.file_path)
    #     init_path=file_info.file_path.split('.')[0]+'.docx'
    #     pythoncom.CoInitialize()
    html = PyDocX.to_html(init_path)
    f = open(html_path, 'w', encoding="utf-8")
    f.write(html)
    f.close()
    shutil.copy(html_path,'D:\\python\\jzyy\\fileserver\\templates\\fileserver\\ol')
    return render(request,'fileserver/ol/%s' % html_name)

#doc->docx转换格式
def doc2x(path):
    pythoncom.CoInitialize()
    in_file=path
    out_file=path.split(".")[0]+".docx"
    word = win32com.client.Dispatch('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=16)
    doc.Close()

#目录更新
# @login_required
# def update_folder(request):
#     fp = a
#     file_path=fp
#     file_list=os.listdir(file_path)
#     had_files=FileInfo.objects.values_list('file_path',flat=True)
#     for file_folder in file_list:
#         if os.path.isdir(os.path.join(fp, file_folder)):
#             if os.path.join(fp, file_folder) not in had_files:
#                 file_info = FileInfo(file_name=file_folder, 
#                         file_size=0, 
#                         file_path=os.path.join(fp, file_folder),
#                         file_type='FOLDER',
#                         load_user=get_user(request),
#                         is_personal=int(B),
#                         folder_name=fp)                  
#                 file_info.save()
#                 file_size1=os.path.getsize(os.path.join(fp, file_folder))
#                 FileInfo.objects.filter(file_path=os.path.join(fp, file_folder)).update(file_size=1 if 0 < file_size1 < 1024 else file_size1 / 1024)
#         else:
#             if os.path.join(fp, file_folder) not in had_files:
#                 file_info = FileInfo(file_name=file_folder, 
#                         file_size=0, 
#                         file_path=os.path.join(fp, file_folder),
#                         file_type=file_folder.split('.')[-1],
#                         load_user=get_user(request),
#                         is_personal=int(B),
#                         folder_name=fp)
#                 file_info.save()
#                 file_size1=os.path.getsize(os.path.join(fp, file_folder))
#                 FileInfo.objects.filter(file_path=os.path.join(fp, file_folder)).update(file_size=1 if 0 < file_size1 < 1024 else file_size1 / 1024)           
#     return HttpResponseRedirect(reverse('fileserver:list1',args=[a]))

# 将游标返回的结果保存到一个字典对象中
# 备用函数
# views.py
def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc],row))
            for row in cursor.fetchall()]

# 读取excel表的内容然后写入数据库
def xq_c(request):
    # 创建数据库连接
    excel_id=request.POST.getlist("d2p_list")
    file_infos = FileInfo.objects.filter(id__in=excel_id)
    for file_info in file_infos:
        conn = pymysql.connect(host='127.0.0.1', user="root", password='password'
                                , database='jzyy', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "insert into fileserver_xqtj(work_id, name, tj_path) values (%s,%s,%s)"
        sql1 = 'SELECT A.name,COUNT(1) num FROM JZYY.FILESERVER_XQTJ A GROUP BY A.name'
        #打开文件
        file = xlrd.open_workbook(file_info.file_path)
        sheet_1 = file.sheet_by_index(0) #根据sheet页的排序选取sheet
        row_content = sheet_1.row_values(0) #获取指定行的数据，返回列表，排序自0开始
        row_number = sheet_1.nrows #获取有数据的最大行数
        for i in range(1,row_number):
            work_id = sheet_1.cell(i,1).value
            name = sheet_1.cell(i,13).value
            tj_path = file_info.file_path
            values = (work_id, name, tj_path)
        #执行sql语句插入数据
            cursor.execute(sql,values)
            conn.commit()
        cursor.execute(sql1)
        # global results
        results = dictfetchall(cursor)
        cursor.close()
        conn.close()
    return render(request,"fileserver/test.html", {"results ": results })

























