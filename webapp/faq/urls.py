from django.conf.urls.defaults import *

urlpatterns = patterns('faq.views',
                       url('newreply','faq_newreply',name='faq-newreply'),
                       url('vote','faq_vote',name='faq-vote'),
                       url('test','faq_test',name='faq-test'),
                       url(r'^$', 'faq_index', name="faq-index"),
)
