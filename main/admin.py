from django.contrib import admin

from main.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = [ "title", "description", "short_description", "date" , "image"]



# admin.site.register(PostAdmin)