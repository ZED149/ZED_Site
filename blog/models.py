from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

# Tag Class
class Tag(models.Model):
    caption = models.CharField(max_length=100)


# Post Class
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=1000)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)


# Author Class
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    posts = models.ForeignKey(Post, on_delete=models.SET_NULL, related_name="posts", null=True)


