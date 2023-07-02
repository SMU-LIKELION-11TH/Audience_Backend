from django import forms

class JPostForm(forms.Form) :
    title = forms.CharField(label='Title')
    content = forms.CharField(label='Content', widget=forms.Textarea)
    apply_condition =forms.
    회사이름검색하기
    평점
    image = forms.ImageField()
    해시태그

class ReportForm(forms.Form):
    content