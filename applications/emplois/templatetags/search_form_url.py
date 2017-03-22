# -*- coding: UTF-8 -*-
from django import template
from django.contrib.sites.shortcuts import get_current_site

register = template.Library()

@register.simple_tag
def seach_form_url(absolute_url="http://127.0.0.1:8000/en/", language_code='en'):
    #import ipdb;ipdb.set_trace()
    url = absolute_url.split('/') #['http:', '', '127.0.0.1:8000', 'en', '']
    url = url[0] +'//' +  url[2] +'/' + language_code + '/'
    return url+"searchJobs/"

