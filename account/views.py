from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy  # 리버스 오류나면 리버스레이지로
from django.http import JsonResponse
import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView, UpdateView

from .models import Userable, Applicant, Employer
from employ.models import Postable
from util.views import update_interest
from .forms import ApplicantCreateForm, EmployerCreateForm, ApplicantUpdateForm, EmployerUpdateForm


# 로그인
class UserLoginView(View):
    template_name = 'account_detail.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        # email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        # 성공
        if user is not None:
            login(request, user=user)
            return redirect('main_view')
        # 실패
        else:
            return redirect('account_login')


# 회원가입
# 구직자
class ApplicantCreateView(CreateView):
    model = Applicant
    template_name = 'account_detail.html'
    form_class = ApplicantCreateForm

    def get_success_url(self):
        return reverse_lazy('signup_finish')

# 구인자
class EmployerCreateView(CreateView):
    model = Employer
    template_name = 'account_detail.html'
    form_class = EmployerCreateForm

    def get_success_url(self):
        return reverse_lazy('signup_finish')

# 회원가입 완료 view
def signup_finish(request):
    if request.method == "GET":
        redirect('signup_finish')
    else:
        redirect('login_view')

# 아이디 찾기 tested
def search_username(request):  # ajax로 받기 (done)
    data = json.loads(request.body)
    email = data['email']
    nickname = data['nickname']

    # 성공
    if Userable.objects.get(email=email, nickname=nickname).exists():
        username = Userable.objects.get(email=email, nickname=nickname).username
        return JsonResponse({'success': True, 'username': username, 'nickname': nickname, 'email': email})
    # 실패
    else:
        return JsonResponse({'success': False, 'error': f'"{email}", "{nickname}" does not exist.'})


# 아이디/비밀번호 찾기 창 view 만들기
# email 대신 username 쓰기

# 비밀번호 찾기 tested
def search_password(request):  # ajax로 변경(done)
    data = json.loads(request.body)
    username = data['username']

    # 성공
    if Userable.objects.get(username=username).exists():
        user = Userable.objects.get(username=username)
        new_password = Userable.objects.make_random_password()
        user.set_password(new_password)
        user.save()

        send_mail(
            f'임시 비밀번호: {new_password}',
            'from@naver.com',  # 임시 계정 만들기
            [user.email],
            fail_silently=False,
        )
        return JsonResponse({'success': True, 'username': username})
    # 실패
    else:
        return JsonResponse({'success': False, 'error': f'"{username}" does not exist.'})


# 마이페이지
@login_required
def account_detail(request):    # ajax로 받기
    if request.user.is_authenticated:
        return JsonResponse({'user': request.user})

@login_required
def my_posts(request):
    if request.user.is_authenticated:
        posts = Postable.objects.order_by('-created_at')[:5]
        return JsonResponse({'post': posts})

@login_required
def my_posts_detail(request):
    if request.user.is_authenticated:
        posts = Postable.objects.all()
        return JsonResponse({'post': posts})

# 비밀번호 확인
@login_required
def check_password(request):
    user = request.user

    if request.method == "POST":
        if request.POST.password == user.password:
            return render(request, '개인 정보 수정 템플릿')
        else:
            return redirect('check_password')
    else:
        return redirect('check_password')

# 비면번호 변경
# render 사용해서 틀렸을 때 context에 error(key값으로 두 개) 넣어서 같은 페이지로 이동 (done)
@login_required
def change_password(request):
    user = request.user
    if request.method == "POST":
        if request.POST.get('password') == request.user.password:
            new_password = request.POST.get('new_password')
            user.password = new_password
            user.save()

            return redirect('account_update')
        else:
            return render(request, '비밀번호 변경 템플릿', {'error': '비밀번호 틀림'})
    else:
        return render(request, 'account_update')


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
        # update_interest 호출
        update_interest(self.request, 'interest')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_valid(form)

# 계정 삭제
@login_required
def delete_user(request):
    if request.method == 'POST':
        if request.POST.get('password') == request.user.password:
            request.user.delete()
            return redirect('login_view')
        else:
            return render(request, '계정 삭제 템플릿', {'error': '비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, '계정 삭제 템플릿')

