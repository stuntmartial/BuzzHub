from django.contrib import admin
from .models import Content , Like , Comment

class ContentAdmin(admin.ModelAdmin):
    list_display = [
        'postId',
        'creator',
        'caption',
        'image',
        'like_count',
        'comment_count',
        'uploaded_time'
    ]

class LikeAdmin(admin.ModelAdmin):
    list_display = [
        'likeId',
        'postId',
        'liked_by'
    ]

class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'commentId',
        'postId',
        'commented_by',
        'comment'
    ]

admin.site.register(Content,ContentAdmin)
admin.site.register(Like,LikeAdmin)
admin.site.register(Comment,CommentAdmin)