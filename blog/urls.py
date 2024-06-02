from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blogIndex, name='blogIndex'),
    path('blog/<int:postId>', singleView, name='singleView'),
    path('contact', contactView, name='blogContact')
]
