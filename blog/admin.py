from django.contrib import admin
from .models import Post, PostComment

# Registered Models for Admin dashboard
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'published_date',
        'views',
        'image',
    )

    ordering = ('published_date',)

class PostCommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'user',
        'date_commented',
    )

admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
