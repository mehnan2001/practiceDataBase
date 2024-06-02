from django.shortcuts import render, get_object_or_404
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
    post = get_object_or_404(Post, pk=postId, pubDate__lte=datetime.now())
    author = User.objects.get(id=post.author.id)
    comments = Comment.objects.filter(post=post)

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
