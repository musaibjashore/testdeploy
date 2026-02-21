from django.contrib import admin

# Register your models here.
from .models import Post,Comment

class CommentInLine(admin.TabularInline):
    model = Comment

class Postadmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

admin.site.register(Post,Postadmin)
admin.site.register(Comment)
