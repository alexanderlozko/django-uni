from django.contrib import admin

from .models import Comment, BackCall, Category, Order

@admin.register(BackCall)
class BackCallAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'message', 'datetime')
    list_filter = ('datetime',)
    search_fields = ('name', 'phone', 'email', 'message', 'datetime')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'datetime', 'published')
    list_filter = ('datetime',)
    search_fields = ('name', 'message')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name','phone', 'email', 'message',)

