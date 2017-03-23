import pytest
from django.core import mail
from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.test import RequestFactory
from mock import patch
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from applications.emplois import views

###to be implemented