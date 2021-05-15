from django.contrib import admin
from .models import Post, Subject


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime', 'author')
    list_display_links = ('title', 'author')
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)
admin.site.register(Subject)
