from django.shortcuts import render, redirect

from applications.blog.models import Post

# Create your views here.


def posts_list(request):
    all_posts_list = Post.objects.all()
    context = {'all_posts_list': all_posts_list}
    return render(request, 'blog/list_view.html', context)
