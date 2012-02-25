from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$', 'blog_index', name="blog-index"),
    url(r'^(?P<page>[0-9]+)$', 'blog_index', name="blog-index"),
    url(r'full/(?P<articleid>[0-9]+)$', 'article_detail', name="blog-articledetail"),
    url(r'archive/$', 'blog_archive', name='blog-archive'),
)
