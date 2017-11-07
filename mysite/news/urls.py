from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import RedirectView

from . views import (
    index,
    registration
)

urlpatterns = [
    url(r'^$', index, name='news'),
    url(r'^register/$', registration, name='registration')
]
