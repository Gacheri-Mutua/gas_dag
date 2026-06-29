from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from dotenv import load_dotenv


from gas_extract import extract_gas_prices
from gas_transform import transform_gas_prices
from gas_load import load_gas_prices

#default arguments
default_args = {
    "owner": "lynn",
    "depends_on_past": "False",
    "start_date": datetime(2026,6,6),
    "retries": 1,
    "retry_delay": timedelta(minutes=8),
}

with DAG(
    "etl_gas_prices_dag",
    description = "A daily ETL pipeline that gets gas prices from CollectAPI, cleans with Pandas, and loads records into PostgreSQL.",
    schedule=timedelta(minutes=60),
    start_date=datetime(2026,6,6),
    catchup=False
) as dag:
    
    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_gas_prices,
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_gas_prices,
    )

    load = PythonOperator(
        task_id="load",
        python_callable=load_gas_prices,
    )

    extract >> transform >> load
    
