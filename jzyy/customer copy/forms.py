from django import forms
from django.forms import ModelForm,models
from .models import CustInfo,CustContact,JobInfo
 
'''客户信息'''

class CustSearchForm(forms.Form):
    cust_style = forms.ChoiceField(label_suffix='',label='客户类型',choices = (('', '请选择'),('普通公司', '普通公司'),('开发中的客户', '开发中的客户'),('已签约的客户','已签约的客户'),('历史客户','历史客户'),('自动生成','自动生成')),widget=forms.Select(attrs={'class': 'form-control form-control-sm '  }),required=False)
    source = forms.ChoiceField(label_suffix='',label='来源',choices = (('', '请选择'),('BD', 'BD'),('公司线索', '公司线索'),('内推','内推')),widget=forms.Select(attrs={'class': 'form-control form-control-sm'  }),required=False)
    profession = forms.ChoiceField(label_suffix='',label='行业',choices = (('', '请选择'),('房地产', '房地产'),('金融', '金融')),widget=forms.Select(attrs={'class': 'form-control form-control-sm'  }),required=False)
    creator = forms.ChoiceField(label_suffix='',label='创建人',choices = (('', '请选择'),( 'wansx','wansx'),('zhoulele', 'zhoulele')),widget=forms.Select(attrs={'class': 'form-control form-control-sm'  }),required=False)
    cust_name = forms.CharField(label_suffix='',label='公司简称',required=False,max_length=50,widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ' }))
    city = forms.ChoiceField(label_suffix='',label='城市',choices = (('', '请选择'),('上海','上海'),('北京', '北京')),widget=forms.Select(attrs={'class': 'form-control form-control-sm'  }),required=False)
    

class CustForm(ModelForm):
    class Meta:
        model = CustInfo
        exclude = ['create_date','creator']
        widgets = {'cust_style':forms.Select(attrs={'class': 'form-control form-control-sm'  }),
                'cust_name' :forms.TextInput(attrs={'class': 'form-control form-control-sm '  }),
                'cust_fullname' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'invoice' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'profession' : forms.Select(attrs={'class': 'form-control form-control-sm'  }),
                'city' : forms.Select(attrs={'class': 'form-control form-control-sm'  }),
                'tel' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'website' : forms.URLInput(attrs={'class': 'form-control form-control-sm'  }),
                'location' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'email' : forms.EmailInput(attrs={'class': 'form-control form-control-sm'  }),
                'finance' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'establish' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'source' :forms.Select(attrs={'class': 'form-control form-control-sm'  }),
                'develop_stage' : forms.Select(attrs={'class': 'form-control form-control-sm'  }),
                'salary_structure' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'products' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'size' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'value' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'competitor' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'worktime' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'welfare1' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                'welfare2' : forms.TextInput(attrs={'class': 'form-control form-control-sm'  }),
                # 'creator' : forms.Select(attrs={'class': 'form-control form-control-sm'  }),
                'nature' : forms.Select(attrs={'class': 'form-control form-control-sm'  }),
                'is_share' : forms.Select(attrs={'class':'form-control form-control-sm'}),
                'work_category' :forms.Select(attrs={'class': 'form-control form-control-sm'  }),
                'introduction': forms.Textarea(attrs={'class':'form-control'}),
                'culture': forms.Textarea(attrs={'class':'form-control'}),
                'interview_process': forms.Textarea(attrs={'class':'form-control'})}



class CustContactForm(ModelForm):
    class Meta:
        model = CustContact
        # fields = '__all__'
        exclude = ['creator']
        widgets = {'cust':forms.Select(attrs={'class': 'form-control form-control-sm'  }),
        'important':forms.Select(attrs={'class': 'form-control form-control-sm','id':'important'  }),
        'contact_name':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'contact_name'  }),
        'position':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'position'   }),
        'contact_mobile':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'contact_mobile'  }),
        'contact_tel':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'contact_tel'  }),
        'qq':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'qq'  }),
        'wechat':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'wechat'  }),
        'gender':forms.Select(attrs={'class': 'form-control form-control-sm','id':'gender'  }),
        'birth':forms.TextInput(attrs={'class': 'form-control form-control-sm' ,'id':'birth' }),
        'nation':forms.TextInput(attrs={'class': 'form-control form-control-sm' ,'id':'nation' }),
        'tips':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'tips'  })}

class JobInfoForm(ModelForm):
    class Meta:
        model = JobInfo
        # fields = '__all__'
        exclude = ['creator']
        widgets = {'create_date':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'create_date'  }),
        'title':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'title'  }),
        'description':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'description'   }),
        'operator':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'operator'  }),
        'status':forms.Select(attrs={'class': 'form-control form-control-sm','id':'status'  })}
