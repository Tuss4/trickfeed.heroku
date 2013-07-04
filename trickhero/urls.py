from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'trickhero.views.trick'),
	url(r'^home/$', 'trickhero.views.trick'),
	url(r'^success/$', 'favo.views.success'),
    url(r'^myfavs/$', 'favo.views.list_fav'),
    url(r'^bye/$', 'trickhero.views.logout'),
    url(r'^login/$', 'trickhero.views.login'),
    url(r'^hello/$','trickhero.views.hi'),
    url(r'^new/$','trickhero.views.new'),
    url(r'^register/$','trickhero.views.register'),
    url(r'^nodice/$','trickhero.views.nodice'),
    url(r'^efav/$','favo.views.edit_fav'),
    url(r'^edit/$','favo.views.del_fav'),
    # Examples:
    # url(r'^$', 'trickhero.views.home', name='home'),
    # url(r'^trickhero/', include('trickhero.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^homebase/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT, 
        }),
    )