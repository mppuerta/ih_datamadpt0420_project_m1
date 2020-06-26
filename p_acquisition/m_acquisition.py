import pandas as pd
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine

# acquisition functions

def acquire():
    engine = create_engine('sqlite:///../data/raw/raw_data_project_m1.db', poolclass = StaticPool)
    rural = pd.read_sql('select\
    country_info.country_code, career_info.normalized_job_code, country_info.rural\
    from country_info\
    join career_info\
    on career_info.uuid = country_info.uuid',
    con = engine)
    rural.to_csv('../data/raw/rural_info_raw.csv', index = False)
    return rural

#This line is supposed to go to the main function:
rural_info = acquire()







