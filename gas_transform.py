import json
import pandas as pd

def transform_gas_prices(**kwargs):
      
      raw_data = kwargs["ti"].xcom_pull(key = 'extract' ,task_ids="extract")
      
      data = json.loads(raw_data)
      cities = data["result"]["cities"]
      #cities = city_gases["cities"]

      df = pd.DataFrame(cities)
      df.rename(columns = {"name":"city_name","midGrade":"mid_grade"}, inplace=True)
      df.drop(columns = ["lowername"], inplace=True)
      
      city_records = df.to_dict(orient = "records")
      kwargs["ti"].xcom_push(key="transform", value = city_records)