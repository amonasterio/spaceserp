import api_key as a
import json
import requests
from organic_results_parser import parse_organic_results, OrganicResult, parse_organic_results_json_file
import pandas as pd

LOCATION="Washington%2CDistrict+of+Columbia%2CUnited+States"
DOMAIN="google.com"
GL="us"
HL="en"
DEVICE="desktop"
PAGE_SIZE="100"
INPUT_CSV="input/queries_list.csv"
# Domain name to check
DOMAIN_TO_CHECK = "eventflare.io"


def buidEndpoint(query):
    endpoint=f"https://api.spaceserp.com/google/search?apiKey={a.API_KEY}&q={query}&location={LOCATION}&domain={DOMAIN}&gl={GL}&hl={HL}&device={DEVICE}&pageSize={PAGE_SIZE}&resultFormat=json"
    return endpoint

df_input=pd.read_csv(INPUT_CSV,header=None)
l_queries=df_input[0].to_list()
df=pd.DataFrame()
for query in l_queries:
    url=buidEndpoint(query)
    print(f"Checking: {query}")
    # Execute the GET request
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        organic_results=parse_organic_results(data)
        find=False
        for result in organic_results:
            if result.is_domain(DOMAIN_TO_CHECK):
                find=True
                new_row={"query":query,"position":result.position, "url": result.link,"title":result.title,"error":""}
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        if not find:
            new_row={"query":query,"position":"101", "url": "-","title":"-","error":""}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        new_row={"query":query,"position":"-", "url": "-","title":"-","error":response.status_code}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
df.to_csv('output/check_positions.csv',index=False)



