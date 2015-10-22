from django.conf.urls import url
from core import views


urlpatterns = [url(r'^$', views.home, name='home'),
               url(r'^(?P<name>[0-9a-zA-Z]+)/status/$',
                   views.status, name='status'),

               url(r'^(?P<name>[0-9a-zA-Z]+)/(?P<pwd>[0-9a-zA-Z]+)/poweron/$',
                   views.poweron, name='poweron'),

               url(r'^(?P<name>[0-9a-zA-Z]+)/(?P<pwd>[0-9a-zA-Z]+)/poweroff/$',
                   views.poweroff, name='poweroff'),

               url(r'^add/$', views.add, name='add'),

               url(r'^unauth/$', views.unauthorized, name='unauthorized'),
               ]
