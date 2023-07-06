from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy #리버스 오류나면 리버스레이지로
from django.http import JsonResponse

from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView, UpdateView

from .models import Userable, Applicant, Employer
from .forms import ApplicantCreateForm, EmployerCreateForm, ApplicantUpdateForm, EmployerUpdateForm

#로그인
class UserLoginView(View):
    template_name = 'users_login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        #성공
        if user is not None:
            login(request, user=user)
            return redirect('main_view')
        #실패
        else:
            return redirect('account_login')

#회원가입
    #구직자
class ApplicantCreateView(CreateView):
    model = Applicant
    template_name = '회원가입.html'
    form_class = ApplicantCreateForm

    def get_success_url(self):
        return reverse_lazy('account_login')

    #구인자
class EmployerCreateView(CreateView):
    model = Employer
    template_name = '회원가입.html'
    form_class = EmployerCreateForm

    def get_success_url(self):
        return reverse_lazy('account_login')

#아이디 찾기 tested
def search_email(request):
    username = request.POST.get('username')

    if request.method == "POST":
        # 성공
        try:
            email = Userable.objects.get(username=username).email
            return JsonResponse({'username': username, 'email': email})
        # 실패
        except Userable.DoesNotExist:
            return JsonResponse({'error': f'User with username "{username}" does not exist.'}, status=404)
    #return redirect('account_login')
    return JsonResponse({'get': username})


#비밀번호 찾기 tested
def search_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Userable.objects.get(email=email)
            new_password = Userable.objects.make_random_password()
            user.set_password(new_password)
            user.save()

            send_mail(
                '청취자들 비밀번호 재설정 메일',
                f'임시 비밀번호: {new_password}',
                '전송할 이메일',
                [email],
                fail_silently=False,
            )

            return redirect('account_login')
        except Userable.DoesNotExist:
            return render(request, '이메일 입력 템플릿', {'error': '해당 이메일 없음'})
    else:
        return render(request, '이메일 입력 템플릿')

#마이페이지
@login_required
def account_detail(request):
    if request.user.is_authenticated:
        return render(request, '마이페이지')
    return redirect('account_login')

# 비밀번호 확인
@login_required
def check_password(request):
    user = request.user

    if request.method == "POST":
        if request.POST.password == user.password:
            return render(request, '비밀번호 수정 페이지')
        else:
            return redirect('account_detail')
    else:
        return redirect('account_detail')

# 비면번호 변경(ajax)
@login_required
def change_password(request):
    if request.method == 'POST' and request.is_ajax():
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    else:
        return JsonResponse({'success': False, 'errors': 'Invalid request'})

# 개인정보 수정

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = '업데이트 템플릿'
    success_url = reverse_lazy('account_detail')

    def get_form_class(self):
        user = self.request.user
        if user.type == 'Applicant':
            return ApplicantUpdateForm
        elif user.type == 'Employer':
            return EmployerUpdateForm

    def form_valid(self, form):
        return super().form_valid(form)
