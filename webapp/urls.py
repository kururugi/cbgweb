from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'homepage.views.home_index', name="homepage-index"),
    url(r'^blog[/]?', include('blog.urls')),
    url(r'^contact[/]?', include('contact.urls')),
    url(r'^message/', include('stdmessage.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bronana/$', 'notepad.views.noteView', {'noteid': 1}),
    url(r'^', include('homepage.urls')),
)
