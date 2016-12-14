#this script is not fully implemented


from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Job, Description


class LatestPostsFeed(Feed):
    title = 'OttawacityJobs'
    link = '/emplois/'
    description = 'New job posts.'

    def items(self):
        return Job.all()[:5]
    def item_name(self, item):
        return item.NAME
    def item_summary(self, item):
        return truncatewords(item.JOB_SUMMARY, 30)
