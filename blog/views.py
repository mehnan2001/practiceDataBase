from django.shortcuts import render
from blog.models import *


def blogIndex(requests):
    posts = Post.objects.all()
    content = {
        'posts': posts
    }
    return render(requests, 'blog/marketing-blog.html', content)


def singleView(requests):
    return render(requests, 'blog/marketing-single.html')


def contactView(requests):
    return render(requests, 'blog/marketing-contact.html')