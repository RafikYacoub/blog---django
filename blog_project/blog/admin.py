from django.contrib import admin

# Register your models here.
from .models import Post, Category, Comment


class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'date']
    list_filter = ['category', 'date']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}


class CatrgoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'date']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CatrgoryAdmin)
admin.site.register(Comment, CommentAdmin)
