from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'homepage.views.home_index', name="homepage-index"),
    url(r'^', include('homepage.urls')),
)
