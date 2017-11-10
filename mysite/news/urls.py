from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import RedirectView

from . views import (
    index,
    registration,
    logout_view
)

urlpatterns = [
    url(r'^$', index, name='news'),
    url(r'^register/$', registration, name='registration'),
    url(r'^logout$', logout_view, name='logout')
]
