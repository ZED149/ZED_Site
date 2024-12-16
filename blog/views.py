from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# home
def home(request):
    return HttpResponse("Salman Ahmad")


# posts
def posts(request):
    return HttpResponse("Posts")


# posts_by_slug
def posts_by_slug(request, slug):
    return HttpResponse(slug)