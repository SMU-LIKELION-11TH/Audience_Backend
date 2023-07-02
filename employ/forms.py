from django import forms

class EPostForm(forms.Form):
    title = forms.CharField(label='Title')
    image = forms.ImageField()
    content = forms.CharField(label='Content', widget=forms.Textarea)
    employ_shape = forms.
    career= forms.
    required_num =forms.IntegerField()
    prefer_condition =forms.CharField(label='Prefer_condition')
    apply_method = forms.CharField()
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    hashtag = forms.CharField()

class QuestionForm(forms.Form):
    title = forms.CharField(label='Title')
    content = forms.CharField(label='Content', widget=forms.Textarea)

class AnswerForm(forms.Form):
    title = forms.CharField(label='Title')
    content = forms.CharField(label='Content', widget=forms.Textarea)
    progress = forms.CharField()



