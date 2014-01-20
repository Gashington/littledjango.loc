from django.contrib import admin
from applications.blog.models import Category, Tag, Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
