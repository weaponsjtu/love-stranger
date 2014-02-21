from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fclover.views.home', name='home'),
    # url(r'^fclover/', include('fclover.foo.urls')),
    url(r'^$', 'activity.views.index'),

    url(r'^signup/$', 'account.views.signup'),
    url(r'^signin/$', 'account.views.signin'),

    url(r'^activity/', include('activity.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
