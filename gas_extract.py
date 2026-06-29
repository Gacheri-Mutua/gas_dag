import os
import json
import http.client
from dotenv import load_dotenv

load_dotenv()

def extract_gas_prices(**kwargs):
    conn = http.client.HTTPSConnection("api.collectapi.com")

    api_key = os.getenv("API_KEY")

    headers = {
        'content-type': "application/json",
        'authorization': f"apikey {api_key}"
        }

    conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")

   
    kwargs["ti"].xcom_push(key="extract", value = data)