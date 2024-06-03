from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from blog.models import *
from django.db.models import Count

category = Tags.objects.values('name', 'repetitions').annotate(disease_count=Count('name')).order_by('-repetitions')[:5]
recentPost = Post.objects.values('id', 'title', 'pubDate', 'image').order_by('-pubDate').filter(
    pubDate__lte=timezone.now(), status=True)[:3]


def blogIndex(requests):
    # posts = Post.objects.all()
    posts = Post.objects.filter(pubDate__lte=timezone.now(), status=True)
    content = {
        'posts': posts,
        'category': category,
        'recentPost': recentPost
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
        'category': category,
        'recentPost': recentPost,
        'posts': posts,
        'prevPost': prevPost,
        'nextPost': nextPost
    }

    return render(requests, 'blog/marketing-single.html', content)


def contactView(requests):
    content = {
        'category': category,
        'recentPost': recentPost
    }
    return render(requests, 'blog/marketing-contact.html', content)
