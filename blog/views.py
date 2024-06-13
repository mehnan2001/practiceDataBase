from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from blog.models import *
from blog.forms import ContactForm


def index(request):
    return render(request, 'index.html')


def blogIndex(requests, **kwargs):
    posts = Post.objects.filter(pubDate__lte=timezone.now(), status=True)

    if kwargs.get('catName') is not None:
        posts = Post.objects.filter(pubDate__lte=timezone.now(), status=True, tags__name=kwargs.get('catName'))
    if kwargs.get('authorId') is not None:
        posts = Post.objects.filter(pubDate__lte=timezone.now(), status=True, author=kwargs.get('authorId'))

    posts = Paginator(posts, 3)

    try:
        pageNumber = requests.GET.get('page')
        posts = posts.get_page(pageNumber)
    except PageNotAnInteger:
        posts = posts.get_page(2)
    except EmptyPage:
        posts = posts.get_page(2)

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

    if requests.method == 'POST':
        form = ContactForm(requests.POST)

        if form.is_valid():
            form = form.cleaned_data
            form['name'] = 'Anonymous'

            ContactUs.objects.create(name=form['name'],
                                     email=form['email'],
                                     phoneNumber=form['phoneNumber'],
                                     subject=form['subject'],
                                     message=form['message'])

            messages.success(requests, "Information was sent successfully!")
            return HttpResponseRedirect('/contact')

    form = ContactForm()
    return render(requests, 'blog/marketing-contact.html', {'form': form})
