from django.contrib import admin
from .models import *
# Register your models here.

class CommentItemInline(admin.TabularInline):
    model = comments
    raw_id_fields = ['post_f']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post_f', 'created_at']

admin.site.register(post, PostAdmin)

admin.site.register(comments, CommentAdmin)

admin.site.register(Category, CategoryAdmin)