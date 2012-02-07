from django.conf.urls.defaults import *

urlpatterns = patterns('homepage.views',
	url(r'^$', 'home_index', name="homepage-index"),
)
