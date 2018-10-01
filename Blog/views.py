from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'Blog/index.html', {'posts': posts})


def post_details(request,pk):
    try:
        post=Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return render(request,'blog/Error 404.html',{})
    return render(request,'blog/details.html',{'post':post})