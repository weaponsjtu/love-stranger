from django.conf.urls import patterns, include, url

from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fclover.views.home', name='home'),
    # url(r'^fclover/', include('fclover.foo.urls')),
    url(r'^$', 'fclover.activity.views.index'),

    url(r'^signup/$', 'fclover.account.views.signup'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^signin/$', 'fclover.account.views.signin'),
	url(r'^signin2/$','fclover.account.views.signin2'),

    url(r'^create/$', 'fclover.activity.views.create'),
    url(r'^delete/$', 'fclover.activity.views.delete'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
)
