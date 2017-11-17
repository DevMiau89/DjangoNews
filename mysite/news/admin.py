# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Article, Comment
from django.contrib import admin

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'article', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']

    class Meta:
        model = Comment


admin.site.register(Article)
admin.site.register(Comment, CommentAdmin)
