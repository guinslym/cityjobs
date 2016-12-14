"""ottawacityjobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin
from django.conf.urls.static import static
import applications.emplois.views as emplois_views
admin.autodiscover()

#from applications.cityjobs.views import *

urlpatterns = [
    #url(r'^emplois/', include('applications.emplois.urls', namespace="emplois")),
    #url(r'^ottawacityjobs/', include('applications.emplois.urls')),

    #url(r'^admin/', admin.site.urls),
    # i18n
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': False}),

      #url(r'^$', views.hello, name='index'),

      url(r'^(?P<pk>[0-9]+)/$', emplois_views.DetailView.as_view(), name='detail'),
      #url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),

      url(r'^stats$', emplois_views.StatsView.as_view(), name='stats'),
      url(r'^searchJobs/$', cache_page(60 * 15)(emplois_views.job_search), name='job_search'),
      url(r'^stats_emplois/$', emplois_views.emplois, name='emplois'),
      url(r'^about$', emplois_views.AboutView.as_view(), name='about'),
      url(r'^all_jobs_posted$', emplois_views.AllJobsView.as_view(), name='all_jobs_posted'),
      url(r'^expiring$', emplois_views.ExpiringSoonView.as_view(), name='expire'),
      url(r'^latest$', emplois_views.LatestView.as_view(), name='latest'),
      url(r'^update/$', emplois_views.update_and_tweets, name='upgrade'),
      url(r'^download/$', emplois_views.download, name='download'),
      url(r'^jobs/$', emplois_views.IndexView.as_view(), name='index'),
      url(r'^$', emplois_views.IndexView.as_view(), name='index'),

]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'applications.emplois.views.handler404'
handler500 = 'applications.emplois.views.handler500'
