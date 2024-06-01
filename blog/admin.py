from django.contrib import admin
from blog.models import *


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'createAt'
    list_display = ('id','subject', 'title', 'author', 'createAt', 'updateAt', 'pubDate', 'status', 'viewCount')
    search_fields = ('subject', 'title', 'content', 'author')
    list_filter = ('subject', 'pubDate')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','firstName', 'lastName', 'birthday', 'email')
    search_fields = ('firstName', 'lastName')



class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','post', 'name', 'email', 'userWebSite', 'createAt')


admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
