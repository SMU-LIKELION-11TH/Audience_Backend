from django.shortcuts import render,redirect
# from .forms import EPostForm,QuestionForm,AnswerForm
from .models import Employ_post, Freepost_e, Question
from account.models import Employer
from django.http import JsonResponse
from util.views import add_hashtag
import json

def employ_post_detail(request,post_id,category) :#게시물 상세(id, 모집공고/Q&A)
    #회사
    if category == "recruitment" : #모집공고 일때
        post = Employ_post.objects.get(id = post_id)
        likes = post.like_set.all().count()
        dislikes = post.dislike_set.all().count()
        context = {
            "post" : post,
            "likes" : likes,
            "dislikes" : dislikes
        }

        return render(request,"employ_list.html",context)
    else:
        return render(request,"employ_list.html")
#
# def create_employ_post(): #구인글 작성
#     #해시태그 저장 함수 utls에서 찾아서 사용
#     if request.method == 'POST':
#         form = EPostForm(request.POST)
#             if form.is_valid():
#
#                 post.save()
#                 added_hashtag = add_hashtag(tag_names)
#                 return redirect('employ_list')
#
#             else:
#                 form = PostForm()
#         return render(request, 'create_employ_post.html')
#         company = Post.objects.filter(title__icontains=’’) #회사 찾기
#
#
# def update_employ_post(): #구인글 수정 #해시태그 저장 함수 utls에서 찾아서 사용
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         form = EPostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('employ_post_detail', post_id=post.id)
#     else:
#         form = PostForm(instance=post)
#     return render(request,)
#
# def delete_employ_post(): #구인글 삭제
#     post = get_object_or_404(Post, id=post_id)
#     post.delete()
#     return redirect('employ_post_detail')
#
#
# def create_employ_free_post(): #구인/자유소통 작성 #해시태그 저장 함수 utls에서 찾아서 사용
#     if request.method == 'POST':
#         form = FreePostForm_e(request.POST)
#             if form.is_valid():
#
#                 post.save()
#                 added_hashtag = add_hashtag(tag_names)
#                 return redirect('employ_list')
#
#             else:
#                 form = FreePostForm_e()
#         return render(request, 'create_employ_post.html')
#
# def update_employ_free_post():#구인/자유소통 수정
#     #해시태그 저장 함수 utls에서 찾아서 사용
#

def QA_list(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post = Employ_post.objects.get(id = data['post_id'])
        QA_list = post.question_set.all()
        page_num = int(data["page_num"])
        QA_list = list(QA_list[5*(page_num-1):5*page_num-1].values())

        context = {
            "QA_List" : QA_list
        }
        return JsonResponse(context)

# def delete_employ_free_post():#구인/자유소통 삭제
#
# def detail_qna(post_id,qna_id): #Q&A 상세(게시물 id,Q&A id)
#     #게시물 요약
#     #질문
#     #답변
#
# def create_question(post_id): #Q&A 질문 작성(게시물 id)
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#             if form.is_valid():
#                 title = form.cleaned_data['title']
#                 content = form.cleaned_data['content']
#                 post = Postable(title=title, content=content)
#                 post.save()
#                 return redirect('employ_list')
#             else:
#                 form = PostForm()
#         return render(request, 'create_question.html')
#
# def delete_question(question_id): #Q&A 질문 삭제(질문 id)
#         question = get_object_or_404(Question, id = question_id)
#         question.delete()
#         return redirect('create_question')
#
#
# def create_answer(question_id): #Q&A 답변 작성(질문 id)
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#             if form.is_valid():
#                 title = form.cleaned_data['title']
#                 content = form.cleaned_data['content']
#                 progress =
#                 post = Postable(title=title, content=content)
#                 post.save()
#                 return redirect('employ_list')
#             else:
#                 form = PostForm()
#         return render(request, 'create_answer.html')
#
# def delete_answer(answer_id): #Q&A 답변 삭제?(답변 id)
#     answer = get_object_or_404(Answer, id = answer_id)
#     answer.delete()
#     return redirect('create_answer')
