# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
