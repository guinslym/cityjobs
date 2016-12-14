from django.contrib.sitemaps import Sitemap
from .models import Job, Description

#TODO I haven't load the SITEMAPS in the SETTINGS...
class JobSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.publish
