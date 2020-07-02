import requests
from bs4 import BeautifulSoup


# Function to build the API and make requests. Input: string, job code. Output: string, job name.
def response_api(job_code):
    return requests.get(f'http://api.dataatwork.org/v1/jobs/{job_code}').json().get('title')


# Function to clean job_title column. It gets a dictionary containing every unique job code in the df. Its keys are
# job codes, its values are job names it iterates over the column.
def jobs_column(rural):
    print('Cleaning Job_name column...')
    job_codes_list = list(rural['Job_name'].unique())
    jobs_dict = {job: response_api(job) for job in job_codes_list}
    rural['Job_name'] = rural['Job_name'].apply(
        lambda job: jobs_dict.get(job) if job is not None else 'Unemployed/NoData')
    print('Job_name clean')
    return rural


# Function to clean rural column. The aim is to get only two values: 'rural' or 'urban'.
def rural_column(rural):
    print('Cleaning Rural column...')
    rural['Rural'] = rural['Rural'].str.lower().replace('city', 'urban') \
        .replace('non-rural', 'urban') \
        .replace('countryside', 'rural') \
        .replace('country', 'rural')
    print('Rural column clean')
    return rural


# Function to import a table via web scrapping, get a dictionary of the info needed to clean the countries column and
# to clean that column.
def countries_dict():
    html = requests.get('https://iban.com/country-codes').content
    soup = BeautifulSoup(html, 'lxml')
    table = [i.text for i in soup.find_all('td')]
    table_dict = {table[i+1]: table[i] for i in range(0, len(table), 4)}
    return table_dict


# Function to clean the countries column.
def countries_clean(rural):
    print('Cleaning countries column...')
    countr_dict = countries_dict()
    rural['Country'] = rural['Country'].apply(lambda country: countr_dict.get(country))
    print('Countries column clean')
    return rural


def wrangling(rural):
    rural_countries_clean = countries_clean(rural)
    rural_jobs_clean = jobs_column(rural_countries_clean)
    rural_rural_clean = rural_column(rural_jobs_clean)
    rural_rural_clean.to_csv('data/processed/clean_rural_info.csv', index=False)
    print('Processed data exported to csv')
    return rural_rural_clean
