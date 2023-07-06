from django.shortcuts import render
from .forms import JPostForm,ReportForm
from .models import Job_post, Freepost_j
from util.views import add_hashtag
import json


# 구직 커뮤니티(구직자들/자유소통 url parameter로 구분)
def job_list(request):
    if request.method == 'GET':
        return render(request,'job_list.html')
    elif request.method == 'POST':
        data = json.loads(request.body)
        category3 = data["category3"]
        category4 = data["category4"]
        page = data["page"]
        if category3 == "applicant" : # 구직자들 일때
                top_posts = Job_post.objects.order_by('-views')[:4] # 조회수 많은거 4개
                posts = Job_post.objects.all()# 전체
                print(data)

                context = {
                    'result': data
                }
                return JsonResponse(context)

        elif category3 == "free_post":# 자유소통 일때
            if category4 == "all" : #all
                top_posts = Freepost_j.objects.order_by('-views')[:4]  #조회수 많은거 4개
                posts = Freepost_j.objects.all()# 전체
                print(data)

                context = {
                    'result': data
                }
                return JsonResponse(context)

def job_post_detail(id,_): #게시물 상세(id)
    #회사정보
    #구직글



def create_job_post() #구직글 작성
# 평점, 해시태그 추가
    #해시태그 저장 함수 utll에서 찾아서 사용
    if request.method == 'POST':
        form = JPostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                ...
                post = Postable(title=title, content=content)
                post.save()
                return redirect('#평점, 해시태그 추가 url')
            else:
                form = JPostForm()
        return render(request, 'create_job_post.html')

def update_job_post()#구직글 수정
    #해시태그 저장 함수 utls에서 찾아서 사용
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = JPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = JPostForm(instance=post)
    return render(request, )

def delete_job_post()#구직글 삭제
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('job_post_detail')

def create_job_free_post(): #구직/자유소통 작성
    #해시태그 저장 함수 utls에서 찾아서 사용

def update_job_free_post(): #구직/자유소통 수정
    #해시태그 저장 함수 utls에서 찾아서 사용

def delete_job_free_post(): #구직/자유소통 삭제


def report(post_id): #신고하기(글 id)
    if request.method == 'POST':
        form = ReportForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data['content']
                post.save()
                return redirect('post_list')
            else:
                form = ReportForm()
        return render(request, 'report.html')