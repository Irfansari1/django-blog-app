from django.contrib import admin

# Register your models here.

from .models import Category, Post, PostView, Comment, Like

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(PostView)
admin.site.register(Comment)