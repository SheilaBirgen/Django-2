from django.contrib import admin
from .models import Following, Post, Comment, Profile

# Register your models here.
admin.site.register(Following)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)