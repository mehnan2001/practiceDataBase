from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blogIndex, name='blogIndex'),
    path('blog/<int:postId>', singleView, name='singleView'),
    path('blog/category/<str:catName>', blogIndex, name='category'),
    path('blog/author/<int:authorId>', blogIndex, name='author'),
    path('contact', contactView, name='blogContact'),
    path('index', index, name='index'),

]
