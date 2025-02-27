from django.contrib import admin

# Register your models here.


from .models import Post, Author, Tag

# PostAdmin
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags")


# AuthorAdmin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email",)

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)