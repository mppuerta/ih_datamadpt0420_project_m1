import requests

# wrangling functions

def response_api(job_code):
    return requests.get(f'http://api.dataatwork.org/v1/jobs/{job_code}').json().get('title')

def jobs_to_dict(rural):
    job_codes_list = list(rural['normalized_job_code'].dropna().unique())
    return {job: response_api(job) for job in job_codes_list}

def wrangling(rural):
    print('Transforming job codes...')
    rural['normalized_job_code'] = rural['normalized_job_code'].apply(lambda job: jobs_to_dict(rural).get(job)
    print('Transformation successful of job codes to names.')
    return rural