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

#is there a 'full.json' file?
def is_there_a_new_json_file():
    import os.path
    if os.path.isfile('data_jobs.json'):
        logger.info("There is a full.json file in the current path")
        return True
    else:
        return False

#load it
def get_the_data_from_this_file():
    with open('data_jobs.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data

def insert_this_job_in_the_db(job):
    logger.info("This job will be added : " +  job.get('POSITION', None))
    salary = job.get('SALARYMAX', None)
    if salary:
        if ',' in salary:
            salary = salary.replace(',', '')
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
    #save Description to db
    #list_emploi.append( emploi.get('JOBREF'))
    #print(emploi_model.jobref)
    emploi_model.save()
    emploi_model.description_set.create(
        KNOWLEDGE = job.get('KNOWLEDGE', None),
        LANGUAGE_CERTIFICATES = job.get('LANGUAGE_CERTIFICATES', None),
        EDUCATIONANDEXP = job.get('EDUCATIONANDEXP', None),
        COMPANY_DESC = job.get('COMPANY_DESC', None),
        POSTDATE =  stringify_object(job.get('POSTDATE', None)),
            )

def check_in_the_db(data):
    for job in data.get('jobs'):
        jobref = job.get('JOBREF')
        result = Job.objects.filter(JOBREF=jobref)
        if result:
            print('Already in the DB')
            logger.info('Already in the DB')
        else:
            logger.info('A new job will be added')
            insert_this_job_in_the_db(job)

def process_it():
    file_exist = is_there_a_new_json_file()
    if file_exist:
        data = get_the_data_from_this_file()
        print('len data ' + str(len(data)))
        logger.info("len data : " + str(len(data)) )
        check_in_the_db(data)
        return True
    return False


def download_ottawa_job_list_content():
    data_en = requests.get('http://www.ottawacityjobs.ca/en/data/')
    data_fr = requests.get('http://www.ottawacityjobs.ca/fr/data/')
    data_en = data_en.json()
    data_fr = data_fr.json()
    data = data_fr
    with open('data_jobs.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=True, sort_keys=True)
    return data

if __name__ == "__main__":
    #Filezilla
    data = download_ottawa_job_list_content()
    #check_in_the_db(data)
    #look online for new data
    # create json file
    #is_there_a_new_json_file()
    #get_the_data_from_this_file()
    process_it()
    pass
