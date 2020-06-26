import pandas as pd
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine


# Function to connect the database and get a dataframe from it. It also exports it to a csv.
def acquire(path):
    engine = create_engine(f'sqlite:///{path}', poolclass=StaticPool)
    raw_rural = pd.read_sql('select\
    country_info.country_code, career_info.normalized_job_code, country_info.rural\
    from country_info\
    join career_info\
    on career_info.uuid = country_info.uuid',
                            con=engine)
    raw_rural.to_csv('data/raw/raw_rural_info.csv', index=False)
    return raw_rural
