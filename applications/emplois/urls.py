# -*- coding: utf-8 -*
from django.conf.urls import url, include

from . import views
from django.views import generic
from django.views.decorators.cache import cache_page
from applications.emplois.views import robot_files
__author__ = 'Guinsly'

app_name = 'emplois'
urlpatterns = [
      #url(r'^$', views.hello, name='index'),
      url(r'^(?P<filename>(robots.txt)|(humans.txt))$', robot_files, name='home-files'),

      url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
      #url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),

      url(r'^stats$', views.StatsView.as_view(), name='stats'),
      url(r'^searchJobs/$', cache_page(60 * 15)(views.job_search), name='job_search'),
      url(r'^stats_emplois/$', views.emplois, name='emplois'),
      url(r'^about$', views.AboutView.as_view(), name='about'),
      url(r'^all_jobs_posted$', views.AllJobsView.as_view(), name='all_jobs_posted'),
      url(r'^expiring$', views.ExpiringSoonView.as_view(), name='expire'),
      url(r'^latest$', views.LatestView.as_view(), name='latest'),
      url(r'^i18n/', include('django.conf.urls.i18n')),
        
      url(r'^download/$', views.download, name='download'),
      url(r'^jobs/$', views.IndexView.as_view(), name='index'),
      url(r'^$', views.IndexView.as_view(), name='index'),

        ]
