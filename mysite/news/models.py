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



