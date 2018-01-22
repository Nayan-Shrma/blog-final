from django.conf.urls import url
from django.contrib import admin

from .views import (
	fullcount_view,
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)
# from .views import *

urlpatterns = [
	url(r'^$', post_list,name = "list"),
    url(r'^create/$', post_create),
    url(r'^full_count/$',fullcount_view,name = "full_count"),

    url(r'^(?P<slug>[\w-]+)/$', post_detail, name ="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update,name = "update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    ]