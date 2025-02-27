from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post

# home
def home(request):
    # fetch all posts from DB
    posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/blog.html", {
        "posts": posts
    })


# posts
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {
        "all_posts": all_posts
    })


# posts_by_slug
def posts_by_slug(request, slug):
    # find the post from db with the slug passed
    # finded = Post.objects.get(slug=slug)
    finded = get_object_or_404(Post, slug=slug)
    return render(request, "blog/single_post.html", {
        "post": finded,
        "post_tags": finded.tags.all()
    })