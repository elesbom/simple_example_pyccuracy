from django.conf.urls.defaults import *
from bookmarks.views import *
from django.views.generic.simple import direct_to_template
import os.path
site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'site_media/(?P<path>.*)$', 'django.views.static.serve', 
                                { 'document_root': site_media }),
    (r'^register/$', register_page),
    (r'^user/(\w+)/$', user_page),
    (r'^fechar_conta/(\w+)$', fechar_conta),
)
