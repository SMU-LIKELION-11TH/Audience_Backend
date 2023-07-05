from django import forms
from account.models import Userable, Applicant, Employer
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class ApplicantCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Applicant
        fields = ['email', 'username', 'password1', 'password2',
                  'interest', 'nickname', 'age', 'gender',
                  'school', 'career']

class EmployerCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employer
        fields = ['email', 'username', 'password1', 'password2',
                  'interest', 'company', 'rating_sum', 'post_num']

class ApplicantUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Applicant
        fields = ['nickname', 'age', 'gender', 'school', 'career']

class EmployerUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Employer
        fields = ['company']