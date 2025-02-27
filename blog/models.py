from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse

# Create your models here.

# Tag Class
class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"
    

# Author Class
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


# Post Class
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=1000)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("posts_slug", args=[self.slug])
    

