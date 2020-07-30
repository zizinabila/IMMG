from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class BlogPost(admin.ModelAdmin):
    list_display = ('category', 'title', 'date_posted', 'author', 'updated_date', 'updated_by')
    ordering = ('date_posted',)
    search_fields = ['title', 'author__username' 'updated_by__username']

@admin.register(Category)
class BlogCategory(admin.ModelAdmin):
    list_display = ('category_code', 'category_desc')
    ordering = ('category_desc',)
    search_fields = ['category_code', 'category_desc']

