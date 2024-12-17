from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# home
def home(request):
    return render(request, "blog/blog.html")


# posts
def posts(request):
    return render(request, "blog/posts.html")


# posts_by_slug
def posts_by_slug(request, slug):
    return render(request, "blog/single_post.html", {
        "page_title": "ZED| Salman Ahmad"
    })