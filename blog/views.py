from django.shortcuts import render
from blog.models import *
from datetime import datetime


def blogIndex(requests):
    # posts = Post.objects.all()
    posts = Post.objects.filter(pubDate__lte=datetime.now())

    content = {
        'posts': posts
    }
    return render(requests, 'blog/marketing-blog.html', content)


def singleView(requests, postId):
    post = Post.objects.filter(pubDate__lte=datetime.now()).get(id=postId)
    author = User.objects.get(id=post.author.id)
    comments = Comment.objects.all()

    post.viewCount += 1
    post.save()

    content = {
        'post': post,
        'author': author,
        'comments': comments
    }

    return render(requests, 'blog/marketing-single.html', content)


def contactView(requests):
    return render(requests, 'blog/marketing-contact.html')
