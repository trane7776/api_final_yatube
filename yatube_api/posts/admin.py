from django.contrib import admin
from .models import Group, Post, Follow, Comment

admin.site.register(Group)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Comment)
