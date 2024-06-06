import operator

from django import template
from blog.models import Post, Tags
from django.utils import timezone
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('blog/include/blog-recentPost.html')
def recentPost():
    posts = Post.objects.values('id', 'title', 'pubDate', 'image').filter(
        pubDate__lte=timezone.now(), status=True)[:3]
    return {'posts': posts}


@register.inclusion_tag('blog/include/blog-popularCategories.html', name='popCat')
def popularCategories(count=5):
    posts = Post.objects.filter(status=True, pubDate__lte=timezone.now())
    category = Tags.objects.all().order_by('name')[:count]
    categoties = {}

    for name in category:
        categoties[name.name] = posts.filter(tags=name).count()

    return {'categoties': dict(sorted(categoties.items(), key=operator.itemgetter(1), reverse=True))}


@register.inclusion_tag('blog/include/blog-subscribe.html')
def subscribe():
    pass


@register.inclusion_tag('includeIndex.html')
def recentPostForIndex(count=3):
    posts = Post.objects.filter(
        pubDate__lte=timezone.now(), status=True)[:count]
    return {'posts': posts}
