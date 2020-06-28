import requests
from bs4 import BeautifulSoup
import lxml.html as lh
import re

# Function to build the API and make requests. Input: string, job code. Output: string, job name.
def response_api(job_code):
    return requests.get(f'http://api.dataatwork.org/v1/jobs/{job_code}').json().get('title')


# Function to clean job_title column. It gets a dictionary containing every unique job code in the df. Its keys are
# job codes, its values are job names it iterates over the column.
def jobs_column(rural):
    print('Cleaning Job_name column...')
    job_codes_list = list(rural['Job_name'].dropna().unique())
    jobs_dict = {job: response_api(job) for job in job_codes_list}
    rural['Job_name'] = rural['Job_name'].apply(lambda job: jobs_dict.get(job))
    print('Job_name clean')
    return rural


# Function to clean rural column. The aim is to get only two values: 'rural' or 'urban'.
def rural_column(rural):
    print('Cleaning Rural column...')
    rural['Rural'] = rural['Rural'].str.lower()
    rural['Rural'] = rural['Rural'].str.replace('city', 'urban')\
        .replace('non-rural', 'urban')\
        .replace('countryside', 'rural')\
        .replace('country', 'rural')
    print('Rural column clean')
    return rural


def cleaning_list(name):
    name1 = re.sub('<td>', '', str(name))
    name2 = re.sub('</td>', '', str(name1))
    return name2

def countries_dict():
    html = requests.get('https://iban.com/country-codes').content
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find(id='myTable').find_all(['tbody'])
    table_list = list(table[0].find_all('td'))
    clean_table_list = list(map(cleaning_list, table_list))
    table_dict = {clean_table_list[i + 1]: clean_table_list[i] for i in range(0, len(clean_table_list), 4)}
    return table_dict

def countries_clean(rural):
    print('Cleaning countries column...')
    countr_dict = countries_dict()
    rural['Country'] = rural['Country'].apply(lambda country: countr_dict.get(country))
    print('Countries column clean')
    return rural


def wrangling(rural):
    rural_jobs_clean = jobs_column(rural)
    rural_rural_clean = rural_column(rural_jobs_clean)
    rural_countries_clean = countries_clean(rural_rural_clean)
    return rural_countries_clean


