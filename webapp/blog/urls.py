from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$', 'blog_index', name="blog-index"),
    url(r'^(?P<page>[0-9]+)$', 'blog_index', name="blog-index"),
)
