from django.contrib import admin
from .models import Post, UserProfile
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(UserProfile)
