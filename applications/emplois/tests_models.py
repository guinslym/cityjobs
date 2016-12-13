import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from applications.emplois.models import Job
from applications.emplois.models import Description


class TestJob:

    ###########################################################
    ##              BEGIN ATTRIBUTES TESTS                   ##
    ###########################################################

    def test_model(self):
        '''
        Test if models exists trying to create an instance
        return:
        '''
        obj = mixer.blend(Job)
        #pytest.set_trace()
        assert obj.pk == 1, 'Should be 1'

    def test_joburl_attr(self):
        #Test name attribute
        obj = mixer.blend(Job)
        assert hasattr(obj, 'JOBURL') == True

    def test_expirydate_attr(self):
        #Test description attribute
        obj = mixer.blend(Job)
        assert hasattr(obj, 'EXPIRYDATE') == True

    def test_salarymax_attr(self):
        #Test description attribute
        obj = mixer.blend(Job)
        assert hasattr(obj, 'SALARYMAX') == True

    def test_salarymin_attr(self):
        #Test description attribute
        obj = mixer.blend(Job)
        assert hasattr(obj, 'SALARYMIN') == True

    def test_salarytype_attr(self):
        #Test description attribute
        obj = mixer.blend(Job)
        assert hasattr(obj, 'SALARYTYPE') == True

    def test_NAME_attr(self):
        #Test description attribute
        obj = mixer.blend(Job)
        assert hasattr(obj, 'NAME') == True

    def test_other_attr(self):
        #Test description attribute
        obj = mixer.blend(Job)
        assert hasattr(obj, 'language') == True
        assert hasattr(obj, 'POSITION') == True
        assert hasattr(obj, 'JOBREF') == True
        assert hasattr(obj, 'JOB_SUMMARY') == True
        assert hasattr(obj, 'POSTDATE') == True
        assert hasattr(obj, 'slug') == True
        assert hasattr(obj, 'tweeted') == True

class TestDescription:

    ###########################################################
    ##              BEGIN ATTRIBUTES TESTS                   ##
    ###########################################################

    def test_model(self):
        '''
        Test if models exists trying to create an instance
        return:
        '''
        obj = mixer.blend(Description)
        #pytest.set_trace()
        assert obj.pk == 1, 'Should be 1'

    def test_attributes(self):
        #Test name attribute
        obj = mixer.blend(Description)
        assert hasattr(obj, 'jobs') == True
        assert hasattr(obj, 'KNOWLEDGE') == True
        assert hasattr(obj, 'LANGUAGE_CERTIFICATES') == True
        assert hasattr(obj, 'EDUCATIONANDEXP') == True
        assert hasattr(obj, 'COMPANY_DESC') == True
        assert hasattr(obj, 'POSTDATE') == True
