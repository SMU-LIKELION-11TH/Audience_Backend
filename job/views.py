from django.shortcuts import render
from .forms import JPostForm, FreePostForm_j
from .models import Job_post, Freepost_j
from account.models import Employer
from util.views import add_hashtag, add_rating
import json
from django.http import JsonResponse

def job_post_detail(request,post_id): #게시물 상세(id)
    #회사
    post = Job_post.objects.get(id=post_id) #구직글
    post.views += 1
    post.save()
    likes = post.like_set.all().count()
    dislikes = post.dislike_set.all().count()
    context = {
        "post": post,
        "likes": likes,
        "dislikes": dislikes
    }
    return render(request, "job_list.html", context)

def create_job_post(request): #구직글 작성
    #해시태그 저장 함수 utll에서 찾아서 사용
    if request.method == 'POST':
        form = JPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.userable = Employer.objects.get(name = request.POST.get("name"))
            post.save()
            # 해시태그들을 list로 바꾸기
            add_hashtag()
            # 평점 추가하기   add_rating
            # 회사 선택하기 	choice_company = Employer.objects.filter(title__icontains=’company’)

            return redirect('job_post_detail', post.id)
        else:
            return render(request, 'create_job_post.html')
    else:
        return render(request, 'create_job_post.html')

def update_job_post(request,id): #구직글 수정
    #해시태그 저장 함수 utls에서 찾아서 사용
    post = get_object_or_404(Job_post, id=id)
    if request.method == 'POST':
        form = JPostForm(request.POST, request.FILES ,instance = post)
        if form.is_valid():
            form.save()
            return redirect('job_post_detail',post.id)
        else:
            return render(request, 'create_job_post.html')

    else:
        return render(request, 'create_job_post.html')

def delete_job_post(request,id): #구직글 삭제
    post = get_object_or_404(Postable, id=id)
    post.delete()
    # post list로 redirect
    return redirect('job_post_detail')

def job_free_post_detail(request,post_id):
    post = Freepost_j.objects.get(id=post_id)
    post.views += 1
    post.save()
    likes = post.like_set.all().count()
    dislikes = post.dislike_set.all().count()
    context = {
        "post": post,
        "likes": likes,
        "dislikes": dislikes
    }
    return render(request, "job_list.html", context)
def create_job_free_post(request): #구직/자유소통 작성 #해시태그 저장 함수 utls에서 찾아서 사용
    if request.method == 'POST':
        form = FreePostForm_j(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.userable = request.user
            post.save()
            # 해시태그들을 list로 바꾸기
            add_hashtag(tag_names)

            return redirect('job_free_post_detail', post.id)
        else:
            return render(request, 'create_job_free_post.html')
    else:
        return render(request, 'create_job_free_post.html')

def update_job_free_post(request,id): #구직/자유소통 수정
    #해시태그 저장 함수 utls에서 찾아서 사용
    post = get_object_or_404(Freepost_j, id=id)
    if request.method == 'POST':
        form = FreePostForm_j(request.POST, request.FILES ,instance = post)
        if form.is_valid():
            form.save()
            return redirect('job_free_post_detail',post.id)
        else:
            return render(request, 'create_job_free_post.html')

    else:
        return render(request, 'create_job_free_post.html')
#
def delete_job_free_post(request,id): #구직/자유소통 삭제
    post = get_object_or_404(Postable, id=id)
    post.delete()
    # post list로 redirect
    return redirect('job_free_post_detail')

def report_create_j(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post = Postable.objects.get(id = data['post_id'])
        content = data['content']
        new = report.objects.create(content = content, postable = post)

        return JsonResponse({})

def search_company(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data["name"]
        companies = list(Employer.objects.filter(name__contains = name).values("name"))
        context = {
            "companies" : companies
        }
        return JsonResponse(context)

