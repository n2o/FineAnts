from django.conf.urls import patterns, include, url
from login.views import *

import login.urls

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'), # If user is not login it will redirect to login page
    url(r'^register/$', register, name='register'),
    url(r'^register/success/$', register_success),
)
