from django.shortcuts import render
from .forms import JPostForm,ReportForm, FreePostForm_j
from .models import Job_post, Freepost_j
from util.views import add_hashtag, add_rating
import json


# # 구직 커뮤니티(구직자들/자유소통 url parameter로 구분)
# def job_list(request):
#     if request.method == 'GET':
#         return render(request,'job_list.html')
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         category3 = data["category3"]
#         category4 = data["category4"]
#         page = data["page"]
#         if category3 == "applicant" : # 구직자들 일때
#                 top_posts = Job_post.objects.order_by('-views')[:4] # 조회수 많은거 4개
#                 posts = Job_post.objects.all()# 전체
#                 print(data)
#
#                 context = {
#                     'result': data
#                 }
#                 return JsonResponse(context)
#
#         elif category3 == "free_post":# 자유소통 일때
#             if category4 == "all" : #all
#                 top_posts = Freepost_j.objects.order_by('-views')[:4]  #조회수 많은거 4개
#                 posts = Freepost_j.objects.all()# 전체
#                 print(data)
#
#                 context = {
#                     'result': data
#                 }
#                 return JsonResponse(context)

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
            post = form.save()
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
    post = get_object_or_404(Postable, id=id)
    if request.method == 'POST':
        form = JPostForm(request.POST, request.FILES)
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
            post = form.save()
            # 해시태그들을 list로 바꾸기
            add_hashtag(tag_names)

            return redirect('job_free_post_detail', post.id)
        else:
            return render(request, 'create_job_free_post.html')
    else:
        return render(request, 'create_job_free_post.html')

def update_job_free_post(request,id): #구직/자유소통 수정
    #해시태그 저장 함수 utls에서 찾아서 사용
    post = get_object_or_404(Postable, id=id)
    if request.method == 'POST':
        form = FreePostForm_j(request.POST, request.FILES)
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