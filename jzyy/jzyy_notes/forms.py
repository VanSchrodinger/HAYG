from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        labels={'text':'Topic'}
        exclude = ['date_added','owner_id','id','is_personal']
        widgets={'text':forms.TextInput(attrs={'class': 'form-control form-control-sm' ,'id':'text1' })}

            

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        labels={'text':'内容','title':'标题'}
        exclude = ['date_added','topic_id','id']
        widgets={
                'text':forms.Textarea(attrs={'class': 'form-control form-control-sm' ,'id':'text','cols':80 }),
                'title':forms.TextInput(attrs={'class': 'form-control form-control-sm' ,'id':'title' })}