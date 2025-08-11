from django.shortcuts import render, redirect, get_object_or_404
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