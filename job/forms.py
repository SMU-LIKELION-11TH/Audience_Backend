from django import forms
from .models import Job_post, Report

class JPostForm(forms.ModelForm) :
    class Meta:
        model = Job_post
        fields = ['title', ' apply_condition', 'content ', 'search_company', 'rating',
                  'image ', #'hashtag ']
class FreePostForm_j(forms.ModelForm):
    class Meta :
        model = Freepost_j
        fields =['title', 'image', 'content', #'hashtag']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['content ']