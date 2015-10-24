from django.conf.urls import url
from core import views


urlpatterns = [url(r'^$', views.home, name='home'),
               url(r'^(?P<name>[0-9a-zA-Z_\-]+)/status/$',
                   views.status, name='status'),

               url(r'^(?P<name>[0-9a-zA-Z_\-]+)/(?P<pwd>[0-9a-zA-Z_\-]+)/poweron/$',
                   views.poweron, name='poweron'),

               url(r'^(?P<name>[0-9a-zA-Z_\-]+)/(?P<pwd>[0-9a-zA-Z_\-]+)/poweroff/$',
                   views.poweroff, name='poweroff'),

               url(r'^add/$', views.add, name='add'),

               url(r'^unauth/$', views.unauthorized, name='unauthorized'),
               ]
