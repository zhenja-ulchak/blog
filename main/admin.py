from django.contrib import admin

from main.models import Post , Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = [ "title", "slug", "category", "description", "short_description", "date" , "image"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = [ "title", "slug"]


# admin.site.register(PostAdmin)