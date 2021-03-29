from django import forms
from django.forms import ModelForm,models
from .models import FileInfo
 
'''
上传表单
'''
class UploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),label='选择文件...',help_text='最大100M',required=False)

class FolderForm(forms.Form):
    folder = forms.CharField(label='文件夹',max_length=100,required=False)

class FileForm(ModelForm):
    class Meta:
        model = FileInfo
        # fields = '__all__'
        exclude = ['file_size','file_path','upload_time','file_type','load_user','is_personal','folder_name']
        widgets = {'file_name':forms.TextInput(attrs={'class': 'form-control form-control-sm','id':'file_name'  })}
