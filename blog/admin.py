from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views', 'status', 'published_date', 'created_date', 'author')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved',  'created_date')
    list_filter = ('post', 'approved')
    search_fields = ['name', 'post']


admin.site.register(Category)
