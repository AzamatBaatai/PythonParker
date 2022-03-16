from django.shortcuts import render

# Create your views here.

# Zdes nastraivaetsya otobrajeniya dannyh

from post.models import Post


def post_list(request):
    posts = Post.objects.all()  # select * from post_posts
    return render(request, 'blog/blog.html', context={'post': posts})