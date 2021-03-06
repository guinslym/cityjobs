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
admin.autodiscover()
from applications.emplois.views import robot_files, update_and_tweets
from django.views.decorators.cache import cache_page
from django.conf.urls.i18n import i18n_patterns

#from applications.cityjobs.views import *

urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', robot_files, name='home-files'),
    url(r'^searchJobs/$', cache_page(60 * 15)('applications.emplois.views.job_search'), name='job_search'),
    url(r'^update/(?P<password>[A-Za-z0-9]+)$', update_and_tweets, name='upgrade'),
]


urlpatterns += i18n_patterns(
    url(r'^emplois/', include('applications.emplois.urls', namespace="emplois")),
    url(r'^', include('applications.emplois.urls')),

    # i18n
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': False}),

)# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'applications.emplois.views.handler404'
handler500 = 'applications.emplois.views.handler500'
