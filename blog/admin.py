from django.contrib import admin
from blog.models import Post, BlogComment
from .forms import PostForm

admin.site.register(BlogComment)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
