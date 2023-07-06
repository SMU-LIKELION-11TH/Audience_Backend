from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comment, Reply
from .forms import CommentForm, ReplyForm
import json

@login_required
def create_comment(request, post_id): # 댓글 생성(ajax)
    if request.method == 'POST':
        data = json.loads(request.body)
        filed_form = data['filed_form']
        temp_form = data['temp_form']
        filed_form = CommentForm(request.POST)
        if filed_form.is_vaild():
            temp_form = filed_form.save(commit=False)
            temp_form.post = Post.objects.get(id = post_id)
            temp_form.save()
        print(data)

        context = {
            'result': data
        }
        return JsonResponse(context)
        # return redirect('detail',post_id) ?????
@login_required
def delete_comment(comment_id,post_id): # 댓글 삭제(ajax)
    if request.method == 'POST':
        data = json.loads(request.body)
        my_comment = data['my_comment']
        my_comment = Comment.objects.get(id = comment_id)
        my_comment.delete()

        print(data)

        context = {
            'result': data
        }
        return JsonResponse(context)
        # return redirect('detail', post_id)
@login_required
def create_reply(request,post_id):# 대댓글 쓰기(ajax)
    if request.method == 'POST':
        data = json.loads(request.body)
        form = data['form ']

        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()
            print(data)

            context = {
                'result': data
            }
            return JsonResponse(context)
    # return redirect('detail',post_id)
@login_required
def delete_reply(reply_id, post_id): # 대댓글 삭제(ajax)
    if request.method == 'POST':
        data = json.loads(request.body)
        my_reply =data['my_reply']
        my_reply = Reply.objects.get(id=reply_id)
        my_reply.delete()
        print(data)

        context = {
            'result': data
        }
        return JsonResponse(context)
        # return redirect('detail', post_id)