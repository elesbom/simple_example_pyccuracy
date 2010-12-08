from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from bookmarks.views import *

import os.path


SITE_MEDIA = os.path.join(
    os.path.dirname(__file__), 'site_media'
)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'site_media/(?P<path>.*)$', 'django.views.static.serve', 
                                { 'document_root': SITE_MEDIA }),
    (r'^register/$', register_page),
    (r'^user/(\w+)/$', user_page),
    (r'^fechar_conta/(\w+)$', fechar_conta),
)
