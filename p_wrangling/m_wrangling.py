import requests

# Function to build the API and make requests. Input: string, job code. Output: string, job name.
def response_api(job_code):
    return requests.get(f'http://api.dataatwork.org/v1/jobs/{job_code}').json().get('title')


# Function to clean job_title column. It gets a dictionary containing every unique job code in the df. Its keys are
# job codes and its values are job names and iterates over the column.
def jobs_column(rural):
    job_codes_list = list(rural['normalized_job_code'].dropna().unique())
    jobs_dict = {job: response_api(job) for job in job_codes_list}
    rural['normalized_job_code'] = rural['normalized_job_code'].apply(lambda job: jobs_dict.get(job))
    return rural


# Function to clean rural column. The aim is to get only to values: 'rural' or 'urban'.
def rural_column(rural):
    rural['rural'] = rural['rural'].str.lower()
    rural['rural'] = rural['rural'].str.replace('city', 'urban')\
        .replace('non-rural', 'urban')\
        .replace('countryside', 'rural')\
        .replace('country', 'rural')
    return rural


def wrangling(rural):
    jobs_column(rural)
    rural_column(rural)
    return rural