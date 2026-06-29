import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def load_gas_prices(**kwargs):

    city_records = kwargs["ti"].xcom_pull(task_ids ="transform", key = "transform")
    cities_df = pd.DataFrame(city_records)

    
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

    cities_df.to_sql("gasprices", con=engine, if_exists= "replace", index=False)
    print("ETL process is complete!")