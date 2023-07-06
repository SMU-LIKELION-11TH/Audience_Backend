from django.shortcuts import render, redirect
from django.http import JsonResponse
from account.models import Employer
from employ.models import Postable, Employ_post
from util.models import Hashtag, Interest, UserInterest
from job.models import Job_post, Freepost
import json
from django.db.models import Q

# 메인화면
def main_view(request):
    employ_posts = Employ_post.objects.order_by('-created_at')[:5]  #구인글 5개
    job_posts = Job_post.objects.order_by('-created_at')[:5]        #구직글 5개
    context = {'employ_posts': employ_posts, 'job_posts': job_posts}

    return render(request, '메인화면 템플릿', context)

# 검색페이지(검색어 get parameter)
# 뷰만 띄움
def search_page(request, category):
    return render(request, '검색 화면 템플릿')

# 검색 결과
# 매개변수로 검색어랑 카테고리 pk로 받아서 검색
# ajax
# 구인 카테고리면 employ에서 구직이면 job에서 자유면 freepost

def search_posts(request):
    data = json.loads(request.body)
    keyword = data['keyword']
    category = data['category']
    board_type = data['board_type']
    post_type = data['post_type']
    search_type = data['search_type']

    if category == "구직":
        if board_type == "구직":
            if search_type == "제목":
                posts = Job_post.objects.filter(title__incontain=keyword)
            elif search_type == "내용":
                posts = Job_post.objects.filter(content__incontain=keyword)
            elif search_type == "제목+내용":
                posts = Job_post.objects.filter(Q(title__incontain=keyword) | Q(content__incontain=keyword))
            elif search_type == "해시태그":
                hashtag = Hashtag.objects.filter(name=keyword)
                posts = Job_post.objects.filter(hashtag=hashtag)
        else:
            if search_type == "제목":
                posts = Freepost.objects.filter(title__incontain=keyword)
            elif search_type == "내용":
                posts = Freepost.objects.filter(content__incontain=keyword)
            elif search_type == "제목+내용":
                posts = Freepost.objects.filter(Q(title__incontain=keyword) | Q(content__incontain=keyword))
            elif search_type == "해시태그":
                hashtag = Hashtag.objects.filter(name=keyword)
                posts = Freepost.objects.filter(hashtag=hashtag)
    elif category == "구인":
        if board_type == "구인":
            if post_type == "관심 분야":
                user = request.user
                interest = UserInterest.objects.filter(userable=user)
                employer = Employer.objects.filter(interest=interest)

                if search_type == "제목":
                    posts = Employ_post.objects.filter(title__incontain=keyword, userable=employer)
                elif search_type == "내용":
                    posts = Employ_post.objects.filter(content__incontain=keyword, userable=employer)
                elif search_type == "제목+내용":
                    posts = Employ_post.objects.filter(Q(title__incontain=keyword, userable=employer)
                                                       | Q(content__incontain=keyword, userable=employer))
                elif search_type == "해시태그":
                    hashtag = Hashtag.objects.filter(name=keyword, userable=employer)
                    posts = Employ_post.objects.filter(hashtag=hashtag)
                elif search_type == "회사":
                    posts = employer.postable.filter(company__incontain=keyword, userable=employer)

            elif post_type == "경력":
                if search_type == "제목":
                    posts = Employ_post.objects.filter(title__incontain=keyword, career='a')
                elif search_type == "내용":
                    posts = Employ_post.objects.filter(content__incontain=keyword, career='a')
                elif search_type == "제목+내용":
                    posts = Employ_post.objects.filter(Q(title__incontain=keyword, career='a')
                                                       | Q(content__incontain=keyword, career='a'))
                elif search_type == "해시태그":
                    hashtag = Hashtag.objects.filter(name=keyword)
                    posts = Employ_post.objects.filter(hashtag=hashtag, career='a')
                elif search_type == "회사":
                    posts = Employ_post.objects.filter(company__incontain=keyword)

            elif post_type == "신입":
                if search_type == "제목":
                    posts = Employ_post.objects.filter(title__incontain=keyword, career='b')
                elif search_type == "내용":
                    posts = Employ_post.objects.filter(content__incontain=keyword, career='b')
                elif search_type == "제목+내용":
                    posts = Employ_post.objects.filter(Q(title__incontain=keyword, career='b')
                                                       | Q(content__incontain=keyword, career='b'))
                elif search_type == "해시태그":
                    hashtag = Hashtag.objects.filter(name=keyword)
                    posts = Employ_post.objects.filter(hashtag=hashtag, career='b')
                elif search_type == "회사":
                    posts = Employ_post.objects.filter(company__incontain=keyword, career='b')

        else:
            if search_type == "제목":
                posts = Freepost.objects.filter(title__incontain=keyword)
            elif search_type == "내용":
                posts = Freepost.objects.filter(content__incontain=keyword)
            elif search_type == "제목+내용":
                posts = Freepost.objects.filter(Q(title__incontain=keyword) | Q(content__incontain=keyword))
            elif search_type == "해시태그":
                hashtag = Hashtag.objects.filter(name=keyword)
                posts = Freepost.objects.filter(hashtag=hashtag)
            elif search_type == "회사":
                posts = Freepost.objects.filter(company__incontain=keyword)

    return JsonResponse({'posts': posts})
