from django.shortcuts import render
from posts.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, template_name="index.html",context={'posts': posts})

def post(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request, template_name="post.html",context={'post':post})

def about(request):
    return render(request, template_name="page-about.html")


def contact(request):
    return render(request, template_name="page-contact.html")
