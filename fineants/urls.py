from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.list_transactions, name='list_transactions'),
#    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
]