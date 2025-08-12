from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages # 예외 메세지 담는 역할
from django.http import JsonResponse
from django.contrib import messages
from .models import Post
# Create your views here.

def index(request):
    return JsonResponse(
        {
            'singer':'BTS',
            'song':['FAKE LOVE', '피땀눈물','DNA']
        },
        json_dumps_params={'ensure_ascii':False}
    )

def list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})

def detail(request, post_id):
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post':post})