from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
import pymysql,os
from .forms import CustForm,CustContactForm,CustSearchForm,JobInfoForm,JobSearchForm
from django.urls import reverse
from django.db import connection
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import CustInfo,CustContact,JobInfo
from django.contrib.auth import get_user
from django.db.models import Q


# Create your views here.
# 新增任务
@login_required
def add_job(request):
    if request.method != "POST":
        form = JobInfoForm(label_suffix='')
    else:
        form = JobInfoForm(request.POST)
        if form.is_valid():
            jb = JobInfo(title=request.POST.get('title'), 
                        description=request.POST.get('description'),
                        create_date=request.POST.get('create_date'),
                        creator=request.user,
                        operator=request.POST.get('operator'),
                        status=request.POST.get('status'))
            jb.save()
            # messages.success(request, "新增成功！")
            return HttpResponse('ok')     
        else:
            print('不合法的表单')
    return render('customer/jobinfo.html',{'form': form})


@login_required
def add_cust(request):  
    if request.method != "POST":
        form = CustForm(label_suffix='')# label_suffix='' 替换了标签的冒号
    else:
        form = CustForm(request.POST)
        if form.is_valid():
            print('yep')
            cust_info = CustInfo(cust_name = form.cleaned_data['cust_name'],
                    cust_fullname = form.cleaned_data['cust_fullname'],
                    invoice = form.cleaned_data['invoice'],
                    profession = form.cleaned_data['profession'],
                    city = form.cleaned_data['city'],
                    tel = form.cleaned_data['tel'],
                    website = form.cleaned_data['website'],
                    location = form.cleaned_data['location'],
                    email = form.cleaned_data['email'],
                    finance = form.cleaned_data['finance'],
                    establish = form.cleaned_data['establish'],
                    source= form.cleaned_data['source'],
                    develop_stage = form.cleaned_data['develop_stage'],
                    salary_structure = form.cleaned_data['salary_structure'],
                    products = form.cleaned_data['products'],
                    size = form.cleaned_data['size'],
                    competitor = form.cleaned_data['competitor'],
                    worktime = form.cleaned_data['worktime'],
                    welfare1 = form.cleaned_data['welfare1'],
                    welfare2 = form.cleaned_data['welfare2'],
                    nature = form.cleaned_data['nature'],
                    is_share = form.cleaned_data['is_share'],
                    work_category = form.cleaned_data['work_category'],
                    introduction = form.cleaned_data['introduction'],
                    culture = form.cleaned_data['culture'],
                    interview_process = form.cleaned_data['interview_process'],
                    cust_style = form.cleaned_data['cust_style'],
                    creator= get_user(request),
                    value=form.cleaned_data['value'])
            cust_info.save()
            return HttpResponseRedirect(reverse('customer:custinfo'))
        else:
            print('fuck2')
    return render(request, "customer/add_cust.html",{'form': form})

@login_required
def edit_info(request,cust_id):  
    if request.method != "POST":
        custinfo2 = CustInfo.objects.get(id=cust_id)
        form = CustForm(instance=custinfo2,label_suffix='')
    else:
        form = CustForm(request.POST)
        if form.is_valid():
            custinfo1 =CustInfo.objects.get(id=cust_id)
            custinfo1.cust_name = form.cleaned_data['cust_name']
            custinfo1.cust_fullname = form.cleaned_data['cust_fullname']
            custinfo1.invoice = form.cleaned_data['invoice']
            custinfo1.profession = form.cleaned_data['profession']
            custinfo1.city = form.cleaned_data['city']
            custinfo1.tel = form.cleaned_data['tel']
            custinfo1.website = form.cleaned_data['website']
            custinfo1.location = form.cleaned_data['location']
            custinfo1.email = form.cleaned_data['email']
            custinfo1.finance = form.cleaned_data['finance']
            custinfo1.establish = form.cleaned_data['establish']
            custinfo1.source= form.cleaned_data['source']
            custinfo1.develop_stage = form.cleaned_data['develop_stage']
            custinfo1.salary_structure = form.cleaned_data['salary_structure']
            custinfo1.products = form.cleaned_data['products']
            custinfo1.size = form.cleaned_data['size']
            custinfo1.competitor = form.cleaned_data['competitor']
            custinfo1.worktime = form.cleaned_data['worktime']
            custinfo1.welfare1 = form.cleaned_data['welfare1']
            custinfo1.welfare2 = form.cleaned_data['welfare2']
            custinfo1.nature = form.cleaned_data['nature']
            custinfo1.is_share = form.cleaned_data['is_share']
            custinfo1.work_category = form.cleaned_data['work_category']
            custinfo1.introduction = form.cleaned_data['introduction']
            custinfo1.culture = form.cleaned_data['culture']
            custinfo1.interview_process = form.cleaned_data['interview_process']
            custinfo1.cust_style = form.cleaned_data['cust_style']
            custinfo1.creator= str(get_user(request))
            custinfo1.value=form.cleaned_data['value']
            custinfo1.save()
            return HttpResponseRedirect(reverse('customer:custinfo'))
        else:
            print('表单不合法！')
    return render(request, "customer/add_cust.html",{'form': form,'cust_id':cust_id})

@login_required
def jobinfo(request): 
    if request.method != "POST":
        form = JobInfoForm(label_suffix='')
        form1 =JobSearchForm(label_suffix='')
        print('现在是get网页')
    else:
        form = JobInfoForm(request.POST)
        if form.is_valid():
            important = form.cleaned_data['important']
            contact_name = form.cleaned_data['contact_name']
            contact = CustContact(important=important, 
                        contact_name=contact_name)                   
            contact.save() 
            return HttpResponseRedirect(reverse('customer:jobinfo'))
        else:
            print('fuck2')
    curr_user=str(request.user)
    companies =JobInfo.objects.filter(creator=curr_user).order_by('id')
    paginator = Paginator(companies,15,3) 
    try:
        num = request.GET.get('index','1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)
    context={'page':number,'paginator':paginator,'form': form,'form1':form1}
    return render(request, 'customer/jobinfo.html', context)

def custsearch(request):
    form = CustContactForm(label_suffix='')
    if request.method != "POST":
        form1 = CustSearchForm(label_suffix='')
        print('现在是get网页')
        companies =CustInfo.objects.all().order_by('-create_date')
    else:
        form1 = CustSearchForm(request.POST)
        if form1.is_valid():
            print('yep')
            cust_style=form1.cleaned_data['cust_style']
            source=form1.cleaned_data['source']
            profession=form1.cleaned_data['profession']
            creator=form1.cleaned_data['creator']
            cust_name=form1.cleaned_data['cust_name']
            city=form1.cleaned_data['city']         
     
        else:
            print('fuck2')
        sql ="select a.*,c.num from jzyy.customer_custinfo a left join (select cust_id,count(*) num from jzyy.customer_custcontact  group by cust_id) c on a.cust_name = c.cust_id where a.cust_style like concat('%%',%s,'%%') and a.source like concat('%%',%s,'%%') and a.profession like concat('%%',%s,'%%') and a.creator like concat('%%',%s,'%%') and a.cust_name like concat('%%',%s,'%%') and a.city like concat('%%',%s,'%%')"
        
    companies =CustInfo.objects.raw(sql,params=[cust_style,source,profession,creator,cust_name,city])
    print(str(CustInfo.objects.raw(sql,params=[cust_style,source,profession,creator,cust_name,city]).query))
    paginator = Paginator(companies,15,3) 
    try:
        num = request.GET.get('index','1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)
    context={'page':number,'paginator':paginator,'form1': form1,'form': form}
    return render(request, 'customer/custinfo.html', context)

@login_required
def add_contact(request):  
    if request.method != "POST":
        form = CustContactForm(label_suffix='')# label_suffix='' 替换了标签的冒号
    else:
        form = CustContactForm(request.POST)
        if form.is_valid():
            important = form.cleaned_data['important']
            contact_name = form.cleaned_data['contact_name']
            contact = CustContact(important=important, 
                        contact_name=contact_name,
                        cust = form.cleaned_data['cust'] ,
                        position  = form.cleaned_data['position'],
                        contact_mobile = form.cleaned_data['contact_mobile'],
                        contact_tel= form.cleaned_data['contact_tel'],
                        qq = form.cleaned_data['qq'],
                        wechat= form.cleaned_data['wechat'],
                        gender = form.cleaned_data['gender'],
                        birth=  form.cleaned_data['birth'],
                        nation= form.cleaned_data['nation'],
                        tips= form.cleaned_data['tips'],
                        creator= get_user(request))                   
            contact.save()                       
            return HttpResponseRedirect('http://127.0.0.1:8000/customer/custinfo/%s#contacts'% C_ID)
            # return HttpResponseRedirect(reverse('customer:custdetails',args=[C_ID]))
        else:
            print('fuck2')
    return render(request, "customer/custdetails.html",{'form': form})

@login_required
def edit_contact(request,contact_id):  
    if request.method != "POST":
        contact1 = CustContact.objects.get(id=contact_id)
        form = CustContactForm(instance=contact1,label_suffix='')
    else:
        form = CustContactForm(request.POST)
        if form.is_valid():
            contact2 = CustContact.objects.get(id=contact_id)
            contact2.important=form.cleaned_data['important'], 
            contact2.contact_name=form.cleaned_data['contact_name']
            contact2.cust = form.cleaned_data['cust'] ,
            contact2.position  = form.cleaned_data['position'],
            contact2.contact_mobile = form.cleaned_data['contact_mobile'],
            contact2.contact_tel= form.cleaned_data['contact_tel'],
            contact2.qq = form.cleaned_data['qq'],
            contact2.wechat= form.cleaned_data['wechat'],
            contact2.gender = form.cleaned_data['gender'],
            contact2.birth=  form.cleaned_data['birth'],
            contact2.nation= form.cleaned_data['nation'],
            contact2.tips= form.cleaned_data['tips'],
            contact2.creator= str(get_user(request))                  
            contact2.save()                       
            return HttpResponseRedirect('http://127.0.0.1:8000/customer/custinfo/%s#contacts'% C_ID)
        else:
            print('fuck2')
    return render(request, "customer/custdetails.html",{'form': form,'contact_id':contact_id})


@login_required
def custdetails(request,cust_id):
    global C_ID
    C_ID = cust_id
    if request.method != "POST":
        form = CustContactForm(label_suffix='')
        form_status = 0
    else:
        form = CustContactForm(request.POST)
        form_status = 1
        if form.is_valid():
            print('form是合法的啦！')
            important = form.cleaned_data['important']
            contact_name = form.cleaned_data['contact_name']
            contact = CustContact(important=important, 
                        contact_name=contact_name)                   
            contact.save() 
            return HttpResponseRedirect(reverse('customer:custdetails'))
    custinfo =CustInfo.objects.get(id=cust_id)
    contacts=custinfo.custcontact_set.all()
    context={'custinfo':custinfo,'contacts':contacts,'form':form,'form_status':form_status}
    return render(request,'customer/custdetails.html',context)

#批量
@login_required
def contact_operation(request):
    if 'delete_list' in request.POST:# 删
        if 'delete_list' in request.POST:
            contact_id=request.POST.getlist("contact_id")
            contacts = CustContact.objects.filter(id__in=contact_id)
            for contact in contacts:
                    contact.delete() 
    return HttpResponseRedirect('http://127.0.0.1:8000/customer/custinfo/%s#contacts'% C_ID)
    # return HttpResponseRedirect(reverse('customer:custdetails',args=[C_ID]))



