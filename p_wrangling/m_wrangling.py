import requests

# wrangling functions

def response_api(job_code):
    return requests.get(f'http://api.dataatwork.org/v1/jobs/{job_code}').json().get('title')

def jobs_to_dict(rural):
    job_codes_list = list(rural['normalized_job_code'].dropna().unique())
    return {job: response_api(job) for job in job_codes_list}

def rural_column(rural):
    rural['rural'] = rural['rural'].str.lower()
    rural['rural'] = rural['rural'].str.replace('city', 'urban')\
        .replace('non-rural','urban')\
        .replace('countryside', 'rural')\
        .replace('country', 'rural')
    return rural


def wrangling(rural):
    print('Transforming job codes...')
    jobs_dict = jobs_to_dict(rural)
    rural['normalized_job_code'] = rural['normalized_job_code'].apply(lambda job: jobs_dict.get(job))
    print('Transformation successful of job codes to names.')
    print(rural)
    rural_column_clean = rural_column(rural)
    print(rural)
    return rural_column_clean