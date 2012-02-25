from django.conf.urls.defaults import *

urlpatterns = patterns('homepage.views',
    url(r'contribute/$', 'contribute', name="contribute"),
)
