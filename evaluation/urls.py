#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/evaluation
'''

from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'seek.views.list_jobs', name='list_jobs'),
    url(r'^detail_jobs/(?P<pk>[0-9]+)$', 'seek.views.detail_jobs', name='detail_jobs')
)