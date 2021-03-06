from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ProfileManager.profile.views.profile', name='profile'),
    url(r'^home/$', 'ProfileManager.profile.views.home', name='home'),
    url(r'^login/$', 'ProfileManager.profile.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/',}, name='logout'),
    url(r'^signup/$', 'ProfileManager.profile.views.signup', name='signup'),
    # url(r'^ProfileManager/', include('ProfileManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('social_auth.urls')),
)

if settings.DEBUG == True:
    urlpatterns += patterns('',
                            url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)