from django.shortcuts import render
from .forms import JPostForm,ReportForm
from employ.models import Postable



# 구직 커뮤니티(구직자들/자유소통 url parameter로 구분)
def job_list(request,category1,):
    if applicant: # 구직자들 일때
        #조회수 많은거 4개
            # 전체


    if job_freepost:# 자유소통 일때
        posts = Postable.objects.all() #all
            #조회수 많은거 4개
            # 전체

def job_post_detail(id,_): #게시물 상세(id)
    #회사
    #구직글



def create_job_post()#구직글 작성
    #해시태그 저장 함수 utls에서 찾아서 사용
    if request.method == 'POST':
        form = JPostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                ...
                post = Postable(title=title, content=content)
                post.save()
                return redirect('post_list')
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

def create_job_free_post():#구직/자유소통 작성
    #해시태그 저장 함수 utls에서 찾아서 사용

def update_job_free_post():#구직/자유소통 수정
    #해시태그 저장 함수 utls에서 찾아서 사용

def delete_job_free_post():#구직/자유소통 삭제


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

