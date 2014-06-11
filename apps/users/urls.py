from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^log-out/$', 'apps.users.views.LogOut', name='logout'),
)
