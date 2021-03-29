from django import forms
from django.forms import ModelForm,models
from .models import OvertimeInfo,WorklogInfo
from users.models import UserInfo
from django.contrib.auth.models import User
 
class OtForm(ModelForm):
    class Meta:
        model = OvertimeInfo
        fields = '__all__'
        widgets = {
        'date':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'date'  }),
        'work_type':forms.Select(attrs={'class': 'form-control form-control-sm','id':'work_type'   }),
        'work_info':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'work_info'  }),
        'name':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'name'  }),
        'expense':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'expense'  }),
        'extra':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'extra'  })}
 
class OtForm1(ModelForm):
    class Meta:
        model = OvertimeInfo
        fields = '__all__'
        widgets = {
        'date':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'date1'  }),
        'work_type':forms.Select(attrs={'class': 'form-control form-control-sm','id':'work_type1'   }),
        'work_info':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'work_info1'  }),
        'name':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'name1'  }),
        'expense':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'expense1'  }),
        'extra':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'extra1'  })}
               
class OtSearchForm(forms.Form):
    name = forms.CharField(label_suffix='',label='姓名',required=False,max_length=50,widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ' }))

#工作日志
class WlForm(ModelForm):#新增
    class Meta:
        model = WorklogInfo
        exclude = ['id','user']
        widgets = {
        'date':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'date'  }),
        'text':forms.Textarea(attrs={'class': 'form-control form-control-sm' ,'id':'text','cols':80 })}

class WlForm1(ModelForm):#修改
    class Meta:
        model = WorklogInfo
        exclude = ['id','user']
        widgets = {
        'date':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'date1'  }),
        'text':forms.Textarea(attrs={'class': 'form-control form-control-sm' ,'id':'text1','cols':80 })}

class WlSearchForm(forms.Form):
    bg_date = forms.CharField(label_suffix='',label='开始日期',required=False,max_length=50,widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ', 'autocomplete':"off",'id':'bg_date' }))#'autocomplete':"off" 取消自动提示历史输入
    en_date = forms.CharField(label_suffix='',label='结束日期',required=False,max_length=50,widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ','autocomplete':"off",'id':'en_date'}))
    keyword = forms.CharField(label_suffix='',label='内容',required=False,max_length=50,widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ','autocomplete':"off",'placeholder':'搜索关键字','id':'keyword'}))

#用户职级维护
class UlForm(ModelForm):#新增
    class Meta:
        model = UserInfo
        exclude = ['id']
        widgets = {
        'username':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'username'  }),
        'level':forms.Select(attrs={'class': 'form-control form-control-sm' ,'id':'level' }),
        'leader':forms.Select(attrs={'class': 'form-control form-control-sm' ,'id':'leader' })}