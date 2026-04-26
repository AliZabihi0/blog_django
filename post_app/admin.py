from django.contrib import admin
from .models import Post, Category, Comment, Message,Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author","show_image")



admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Like)
