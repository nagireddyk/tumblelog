from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from tumblelog.models import Post
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
        queryset=Post.objects.all(),
        context_object_name="posts_list"),
        name="home"
    ),
    url(r'^post/(?P<slug>[a-zA-Z0-9-]+)/$', DetailView.as_view(
        queryset=Post.objects.all(),
        context_object_name="post"),
        name="post"
    ),
    url(r'^admin/', include(admin.site.urls)),
)