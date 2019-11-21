from django.contrib import admin

from .models import Comment, BackCall

@admin.register(BackCall)
class BackCallAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'message', 'datetime', 'datetime')
    list_filter = ('datetime',)
    search_fields = ('name', 'phone', 'email', 'message', 'datetime')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment', 'datetime', 'published')
    list_filter = ('datetime',)
    search_fields = ('author', 'comment')
