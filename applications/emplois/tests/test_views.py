import pytest
from django.core import mail
from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.test import RequestFactory
from mock import patch
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from applications.emplois import views


class TestIndexView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        # setting the Language
        req.LANGUAGE_CODE = "en"
        req.user = AnonymousUser()

        resp = views.IndexView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'

class LatestView:
    def test_content(self):
        req = RequestFactory().get('/')
        # setting the Language
        req.LANGUAGE_CODE = "en"

        resp = views.LatestView.as_view()(req)
        pytest.set_trace()# verify the content of the object <resp>
        pass #assert resp.status_code == 200, 'Should be callable by anyone'

#Test urls resolve also....