from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from blog.models import *


def index(request):
    return render(request, 'index.html')
def blogIndex(requests, **kwargs):
    posts = Post.objects.filter(pubDate__lte=timezone.now(), status=True)

    if kwargs.get('catName') is not None:
        posts = Post.objects.filter(pubDate__lte=timezone.now(), status=True, tags__name=kwargs.get('catName'))
    if kwargs.get('authorId') is not None:
        posts = Post.objects.filter(pubDate__lte=timezone.now(), status=True, author=kwargs.get('authorId'))

    content = {
        'posts': posts,
    }
    return render(requests, 'blog/marketing-blog.html', content)


def singleView(requests, postId):
    global prevIndex
    posts = Post.objects.all().filter(status=True, pubDate__lte=timezone.now())
    post = get_object_or_404(posts, pk=postId)

    author = User.objects.get(id=post.author.id)
    comments = Comment.objects.filter(post=post)

    post.viewCount += 1
    post.save()

    prevPost = None
    nextPost = None
    for i, element in enumerate(posts):
        if element == post:
            prevIndex = i - 1
            nextIndex = i + 1

            if prevIndex >= 0:
                prevPost = posts[prevIndex]
            else:
                prevPost = None

            if nextIndex <= len(posts) - 1:
                nextPost = posts[nextIndex]
            else:
                nextPost = None

    content = {
        'post': post,
        'author': author,
        'comments': comments,
        'prevPost': prevPost,
        'nextPost': nextPost
    }

    return render(requests, 'blog/marketing-single.html', content)


def contactView(requests):
    return render(requests, 'blog/marketing-contact.html')
