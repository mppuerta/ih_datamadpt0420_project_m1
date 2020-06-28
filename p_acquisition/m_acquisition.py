import pandas as pd
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine


# Function to connect the database and get a dataframe from it. It also exports it to a csv.
def acquire(path):
    print('Connecting database...')
    engine = create_engine(f'sqlite:///{path}', poolclass=StaticPool)
    raw_rural = pd.read_sql("select\
    country_info.country_code as 'Country', career_info.normalized_job_code as 'Job_name', country_info.rural as 'Rural'\
    from country_info\
    join career_info\
    on career_info.uuid = country_info.uuid",
    con=engine)
    raw_rural.to_csv('data/raw/raw_rural_info.csv', index=False)
    print('Database connected')
    return raw_rural


