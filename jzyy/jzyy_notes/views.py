from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404,StreamingHttpResponse,HttpResponse
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.views.generic.edit import FormView
from .forms import TopicForm,EntryForm
from .models import Topic,Entry
from fileserver.models import FileInfo
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os
import datetime


# 主页
def index(request):
    return render(request,'jzyy_notes/index.html') 

#个人办公
@login_required
def topics(request,num):
    global TOPIC_NUM
    TOPIC_NUM =num
    if num=='1':
        topics=Topic.objects.filter(owner=request.user,is_personal=num).order_by('date_added')
        context={'topics':topics}
    else:
        topics=Topic.objects.filter(is_personal=num).order_by('date_added')
    context={'topics':topics}
    return render(request,'jzyy_notes/topics.html',context)


#搜索框
@login_required
def search(request):
    keyStr = request.GET.get('mykey')
    topic_list =Topic.objects.filter(text__icontains=keyStr)
    file_list = FileInfo.objects.filter(file_name__icontains=keyStr)
    return render(request, 'jzyy_notes/search.html', {'topic_list': topic_list,'file_list':file_list})

# 显示单个主题及其所有条目
@login_required
def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    form=TopicForm()
    form1=EntryForm()
    if topic.owner !=request.user:
        if topic.is_personal == 1:
            raise Http404 
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries,'form':form,'form1':form1}
    return render(request,'jzyy_notes/topic.html',context)

# 添加个人-新主题
@login_required
def new_topic(request):  
    if request.method !='POST':
        form=TopicForm()
    else:
        form=TopicForm(request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.is_personal=TOPIC_NUM
            new_topic.save()
            return HttpResponseRedirect(reverse('jzyy_notes:topics',args=[TOPIC_NUM]))
    context={'form':form}
    return render(request,'jzyy_notes/new_topic.html',context)


# 添加新条目
@login_required
def new_entry(request,topic_id):
    
    topic=Topic.objects.get(id=topic_id)
    if request.method !='POST':
        form=EntryForm()
    else:
        form=EntryForm(request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return HttpResponseRedirect(reverse('jzyy_notes:topic',args=[topic_id]))
    context={'topic':topic,'form':form}
    return render(request,'jzyy_notes/new_entry.html',context)

# 编辑条目
@login_required
def edit_entry(request):
    entry_id =request.POST.get('id')
    print(entry_id)
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if topic.owner != request.user:
        raise Http404    
    if request.method != "POST":
        form1=EntryForm(instance=entry,label_suffix='')
    else:
        form1 = EntryForm(request.POST)
        # if form1.is_valid():
        et = Entry(id=request.POST.get('id'), 
                    text=request.POST.get('text'), 
                    title=request.POST.get('title'),
                    topic_id=request.POST.get('topic_id'),
                    date_added=datetime.datetime.now())
        et.save()
        # messages.success(request, "修改成功！")
        return HttpResponse('ok')
        # else:
        #     print('表单不合法！')
    context={'entry':entry,'topic':topic,'form1':form1}
    return render(request,'jzyy_notes/edit_entry.html',context)

# 编辑主题
@login_required
def edit_topic(request):
    form1=EntryForm()
    topic_id =request.POST.get('id')
    print(topic_id)
    topic=Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method !='POST':
        form=TopicForm(instance=topic,label_suffix='')
    else:
        form=TopicForm(request.POST)
        et = Topic(id=request.POST.get('id'), 
                    text=request.POST.get('text'), 
                    owner_id=topic.owner_id,
                    is_personal=topic.is_personal,
                    date_added=datetime.datetime.now())
        et.save()        
        return HttpResponse('ok')
    context={'topic':topic,'form':form,'form1':form1}
    return render(request,'jzyy_notes/edit_topic.html',context)
