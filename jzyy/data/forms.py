from django import forms
from django.forms import ModelForm,models
from .models import CrmExamInfo
 
'''
上传表单
'''
class UploadForm(forms.Form):# 支持多文件上传
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),label='选择文件...',help_text='最大100M',required=False)

class FolderForm(forms.Form):
    folder = forms.CharField(label='文件夹',max_length=100)

class CrmForm(ModelForm):
    class Meta:
        model = CrmExamInfo
        # fields = '__all__'
        exclude = ['create_date']
        widgets = {
        'name':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'name'  }),
        'user_code':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'user_code'   }),
        'exam_name':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'exam_name'  }),
        'time_limit':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'time_limit'  }),
        'times':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'times'  }),
        'real_times':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'real_times'  }),
        'point':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'point'  })}

class CrmSearchForm(forms.Form):
    name = forms.CharField(label_suffix='',label='考生姓名',required=False,max_length=50,widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ' }))

class ShineSearchForm(forms.Form):
    source_name = forms.CharField(label_suffix='',label='扫描项名称',required=False,max_length=50,widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ' }))
    busi_name = forms.CharField(label_suffix='',label='业务名称',required=False,max_length=50,widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ' }))
    app_id = forms.ChoiceField(label_suffix='',label='渠道',choices = (('', '请选择'),('HAGMSYS', '集中柜面'),('PC_WT', '网厅'),('MO_ZT','掌厅'),('MO_HY', '手机徽赢'),('MO_ZY', '手机智赢'),('MO_SC','手机商城'),('PC_SC','PC商城'),('PC_HY','PC徽赢'),('MO_YJ','手机赢家'),('PC_TZYJ','投资赢家'),('PC_QQB','PC期权宝'),('MP_QQB','手机期权宝'),('MP_QQB','手机期权宝'),('PC_TG','投顾平台')),widget=forms.Select(attrs={'class': 'form-control form-control-sm'  }),required=False)
    # app_id = forms.MultipleChoiceField(label_suffix='',label='渠道',choices = (('HAGMSYS', '集中柜面'),('PC_WT', '网厅'),('MO_ZT','掌厅'),('MO_HY', '手机徽赢'),('MO_ZY', '手机智赢'),('MO_SC','手机商城'),('PC_SC','PC商城'),('PC_HY','PC徽赢'),('MO_YJ','手机赢家'),('PC_TZYJ','投资赢家'),('PC_QQB','PC期权宝'),('MP_QQB','手机期权宝'),('MP_QQB','手机期权宝'),('PC_TG','投顾平台')),widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-sm','id': 'sel_search_orderstatus' }),required=False)
    is_ecimc = forms.ChoiceField(label_suffix='',label='是否无纸化',choices = (('', '请选择'),('已无纸化','是'),('未无纸化','否')),widget=forms.Select(attrs={'class': 'form-control form-control-sm'  }),required=False)