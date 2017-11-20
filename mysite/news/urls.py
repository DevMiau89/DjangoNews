from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import RedirectView

from . views import (
    index,
    registration,
    logout_view,
    add_article,
    article_detail,
    contact
)

urlpatterns = [
    url(r'^$', index, name='news'),
    url(r'^register/$', registration, name='registration'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^add_article/$', add_article, name='add_article'),
    url(r'^article/(?P<id>\d+)/$', article_detail, name='article'),
    url(r'^contact/$', contact, name='contact')
]
