from django.contrib import admin

from .models import Forum, Comment

class CommentInLine(admin.TabularInline):
    model = Comment

class ForumAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

admin.site.register(Forum, ForumAdmin)
admin.site.register(Comment)