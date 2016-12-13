# -*- coding: utf-8 -*-

import json
import requests
import urllib
from applications.emplois.models import Job, Description
from dateutil.parser import *
import logging
logger = logging.getLogger(__name__)

def stringify_object(data):
    '''
    return a String version of a date
    '''
    expirydate = parse(data)
    expirydate = str(expirydate).split(' ')[0]
    return expirydate

def insert_this_job_in_the_db(job):
    """
    Insert the Job that we fetch from OttawaJobs to the DB
    """
    logger.info("This job will be added : " +  job.get('JOBREF', None))
    print("This job will be added : {0}".format(job.get('JOBREF', None)))
    salary = job.get('SALARYMAX', None)
    if salary:
        if ',' in salary:
            salary = salary.replace(',', '')

    #create model object
    emploi_model = Job(
        JOBURL = job.get('JOBURL', None),
        EXPIRYDATE =  stringify_object(job.get('EXPIRYDATE', None)),
        POSTDATE =  stringify_object(job.get('POSTDATE', None)),
        SALARYMAX =  job.get('SALARYMAX', None),
        SALARYMIN =  job.get('SALARYMIN', None),
        SALARYTYPE = job.get('SALARYTYPE', None),
        NAME =  job.get('NAME', None),
        language = job.get('JOBREF', None).split('-')[2],
        POSITION =  job.get('POSITION', None),
        JOBREF = job.get('JOBREF', None),
        JOB_SUMMARY =job.get('JOB_SUMMARY', None),
    )
    emploi_model.save()

    #save Description to db
    emploi_model.description_set.create(
        KNOWLEDGE = job.get('KNOWLEDGE', None),
        LANGUAGE_CERTIFICATES = job.get('LANGUAGE_CERTIFICATES', None),
        EDUCATIONANDEXP = job.get('EDUCATIONANDEXP', None),
        COMPANY_DESC = job.get('COMPANY_DESC', None),
        POSTDATE =  stringify_object(job.get('POSTDATE', None)),
            )

def check_in_the_db(data):
    """
    Check if we have already have this Job id (jobref) in
    the db
    """
    for job in data.get('jobs'):
        jobref = job.get('JOBREF')
        result = Job.objects.filter(JOBREF=jobref)
        if result:
            print('Already in the DB {0}'.format(jobref))
            logger.info('Already in the DB ' + jobref)
        else:
            logger.info('A new job will be added {0}'.format(jobref))
            insert_this_job_in_the_db(job)

def download_ottawa_job_list_content():
    urls = ['http://www.ottawacityjobs.ca/en/data/',
           'http://www.ottawacityjobs.ca/fr/data/']
    for url in urls:
        data = requests.get(url)
        data = data.json()
        check_in_the_db(data)
    with open('data_jobs.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=True, sort_keys=True)
    return data

if __name__ == "__main__":
    #Filezilla
    data = download_ottawa_job_list_content()
    #check_in_the_db(data)
    #look online for new data
    # create json file
    pass
