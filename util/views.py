from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy #리버스 오류나면 리버스레이지로
from django.http import JsonResponse

from .models import Like, Dislike, Interest, Hashtag
from employ.models import Postable


def add_like(request, post_id):
    user = request.user
    post = Postable.objects.get(id=post_id)

    like, created = Like.objects.get_or_create(user=user, postable=post)

    # 좋아요 있으면
    if not created:
        # 좋아요 취소
        like.delete()
        likes_count = Like.objects.filter(postable=post).count()
        dislikes_count = Dislike.objects.filter(postable=post).count()
        return JsonResponse({'likes_count': likes_count, 'dislikes_count': dislikes_count,
                             'is_liked': False, 'is_disliked': False})

    # 싫어요 있으면
    try:
        dislike = Dislike.objects.get(user=user, postable=post)
        # 싫어요 취소
        dislike.delete()
    except Dislike.DoesNotExist:
        pass

    likes_count = Like.objects.filter(postable=post).count()
    dislikes_count = Dislike.objects.filter(postable=post).count()
    return JsonResponse({'likes_count': likes_count, 'dislikes_count': dislikes_count,
                         'is_liked': True, 'is_disliked': False})

def add_dislike(request, post_id):
    user = request.user
    post = Postable.objects.get(id=post_id)

    dislike, created = Dislike.objects.get_or_create(user=user, postable=post)

    # 싫어요 있으면
    if not created:
        # 싫어요 취소
        dislike.delete()
        likes_count = Like.objects.filter(postable=post).count()
        dislikes_count = Dislike.objects.filter(postable=post).count()
        return JsonResponse({'likes_count': likes_count, 'dislikes_count': dislikes_count,
                             'is_liked': False, 'is_disliked': False})

    # 좋아요 있으면
    try:
        like = Like.objects.get(user=user, postable=post)
        # 좋아요 취소
        like.delete()
    except Like.DoesNotExist:
        pass

    likes_count = Like.objects.filter(postable=post).count()
    dislikes_count = Dislike.objects.filter(postable=post).count()
    return JsonResponse({'likes_count': likes_count, 'dislikes_count': dislikes_count,
                         'is_liked': False, 'is_disliked': True})

# 평점 추가/변경
# 구직 게시물 create, update에 추가, 변경 기능을 넣는게 좋을 듯
# 구직 게시물에 mapping된 postable 수를 저장하는 필드(post_num)를 만들고 rating/post_num으로 평균 rating을 나타낼 수 있을 듯
def add_rating(request, post_id):
    post = Postable.objects.get(post_id=post_id)
    # 평점 추가
    post.employer.rating_sum += post.rating
    post.employer.post_num += 1
    # 평점 변경(게시물 update뷰에서 처리)
    if request.method == "GET":
        post.employer.rating_sum -= post.rating
        return redirect("게시물 수정 url")
    else:
        post.employer.rating_sum += request.POST.get('new_rating')
        return redirect("게시물 url", post_id=post_id)

# 관심분야 set
def update_interest(request):
    user = request.user
    # 관심분야 clear
    user.interest.clear()
    # 다시 전부다 연결
    new_interests = request.POST.getlist('new_interests')

    if new_interests:
        for interest_id in new_interests:
            interest = Interest.objects.get(id=interest_id)
            user.interest.add(interest)
        return redirect('마이 페이지')
        #return JsonResponse()
    else:
        error_message = "하나 이상 선택하세요"
        return render(request, 'error.html', {'error_message': error_message})
        # return JsonResponse({'success': False, 'errors': 'Invalid request'})

# 해시태그 생성(게시물 id)
def add_hashtag(request, post_id):
    post = Postable.objects.get(id=post_id)
    hashtag_list = Hashtag.objects.filter(postable=post_id)
    #이미 있는지 확인
    for post_hashtag in hashtag_list:
        # 없으면 추가
        hashtag, created = Hashtag.objects.get_or_create(name=post_hashtag)
        # 게시물이랑 연결
        hashtag.postable.add(post)

    return redirect('게시물', post_id=post_id) #연결
