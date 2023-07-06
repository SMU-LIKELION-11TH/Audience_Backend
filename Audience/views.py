from django.shortcuts import render, redirect
from django.http import JsonResponse
from employ.models import Postable, Employ_post
from job.models import Job_post

# 메인화면
def main_view(request):
    employ_posts = Employ_post.objects.order_by('-created_at')[:5]  #구인글 5개
    job_posts = Job_post.objects.order_by('-created_at')[:5]        #구직글 5개
    context = {'employ_posts': employ_posts, 'job_posts': job_posts}

    return render(request, '메인화면 템플릿', context)

# 검색페이지(검색어 get parameter)
# def search_page(request):
#     keyword = request.POST.get('keyword')
#
#     board_type = request.GET.get('board_type')
#     post_type = request.GET.get('post_type')
#     employ_post_type = request.GET.get('employ_post_type')
#     if board_type:
#         if post_type:
#             if employ_post_type:
#                 posts = .objects.filter(title__icontains=keyword)


# 검색 결과
# def search_posts(request):
#     keyword = request.GET.get('keyword')
#     board_type = request.GET.get('board_type')



    #data
        # all/구직/구인
        # 구인글/자유소통, 구직자들/자유소통

        # 구인 -> 관심분야/신입/경력
        # 구직 -> all

        # 분류 -> all/제목/...

