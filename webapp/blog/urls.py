from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$', 'blog_index', name="blog-index"),
)
