from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'trickhero.views.trick'),
	url(r'^home/$', 'trickhero.views.trick'),
    # Examples:
    # url(r'^$', 'trickhero.views.home', name='home'),
    # url(r'^trickhero/', include('trickhero.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^homebase/', include(admin.site.urls)),
)
