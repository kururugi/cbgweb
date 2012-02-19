from django.conf.urls.defaults import *

urlpatterns = patterns('stdmessage.views',
    url(r'^(?P<msgtype>[a-z]+)/(?P<redirect>.+)$', 'info_message', name='info_output'),
)
