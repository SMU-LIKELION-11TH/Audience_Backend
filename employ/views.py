from django.shortcuts import render,redirect
from .forms import EPostForm,QuestionForm,AnswerForm
from .models import Postable



# 구인 커뮤니티(구인글/자유소통, all/관심분야/경력/신입 url parameter로 구분)
def employ_list(request,category1,category2):
    if category1== employ_post: # 구인글 일때
        #all
            def get_top_4_posts():
                top_posts = Postable.objects.order_by('-views')[:4]
                return top_posts #조회수 많은거 4개
            posts = Postable.objects.all() # 전체
            context = {
                'posts' : posts,
            }
            return renderr(request, '', context)

        #관심분야
            #조회수 많은거 4개
            # 전체
        #경력/신입
            #조회수 많은거 4개
            # 전체
    if category2 == free_post: # 자유소통 일때
         #all
            #조회수 많은거 4개
            # 전체


def employ_post_detail(id,_) #게시물 상세(id, 모집공고/Q&A)
    #회사
    if #모집공고 일때
        #구인글
    if #Q&A일때
        #Q&A list

def create_employ_post(): #구인글 작성
    #해시태그 저장 함수 utls에서 찾아서 사용
    if request.method == 'POST':
        form = EPostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                post = Postable(title=title, content=content)
                ...
                post.save()
                return redirect('employ_list')
            else:
                form = PostForm()
        return render(request, 'create_employ_post.html')

def update_employ_post(): #구인글 수정
    #해시태그 저장 함수 utls에서 찾아서 사용
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = EPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('employ_post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request,)

def delete_employ_post(): #구인글 삭제
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('employ_post_detail')


def create_employ_free_post(): #구인/자유소통 작성
    #해시태그 저장 함수 utls에서 찾아서 사용

def update_employ_free_post():#구인/자유소통 수정
    #해시태그 저장 함수 utls에서 찾아서 사용

def delete_employ_free_post():#구인/자유소통 삭제

def detail_qna(post_id,qna_id): #Q&A 상세(게시물 id,Q&A id)
    #게시물 요약
    #질문
    #답변

def create_question(post_id): #Q&A 질문 작성(게시물 id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                post = Postable(title=title, content=content)
                post.save()
                return redirect('employ_list')
            else:
                form = PostForm()
        return render(request, 'create_question.html')

def delete_question(question_id): #Q&A 질문 삭제(질문 id)
        question = get_object_or_404(Question, id = question_id)
        question.delete()
        return redirect('create_question')


def create_answer(question_id): #Q&A 답변 작성(질문 id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                progress =
                post = Postable(title=title, content=content)
                post.save()
                return redirect('employ_list')
            else:
                form = PostForm()
        return render(request, 'create_answer.html')

def delete_answer(answer_id): #Q&A 답변 삭제?(답변 id)
    answer = get_object_or_404(Answer, id = answer_id)
    answer.delete()
    return redirect('create_answer')
