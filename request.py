from typing import List
import requests
import json
from pprint import pprint
from csv import DictReader
from ast import literal_eval


BASE_URL = "http://localhost:9200"
DATA_STREAM = "gold-1"
RESULTS_QTD = 20
HEADERS = {"Content-Type": "application/json"}

url_get = f"{BASE_URL}/{DATA_STREAM}/_search"
url_post = f"{BASE_URL}/{DATA_STREAM}/_doc"
url_put = f"{BASE_URL}/{DATA_STREAM}/_bulk"


json_get = {"size":RESULTS_QTD,"query": {"match": {"Category": "Asian"}}}
json_get_all = {"query": {"match_all": {}}}

json_post = {"name": "ana", "age": 50}
json_put = [{"name": "carla"}, {"name": "sara"}]


def get_request(json_data: dict, url):
    r = requests.get(url=url, headers=HEADERS, data=json.dumps(json_data))
    return r.json()


def post_request(json_data: dict, url):
    r = requests.post(url=url, headers=HEADERS, data=json.dumps(json_data))
    return r.json()


def put_request(json_list: List[dict], url):
    final_list = []

    for i in json_list:
        final_list.append({"create": {}})
        final_list.append(i)

    data = '\n'.join([json.dumps(i) for i in final_list]) + '\n'
    r = requests.put(url=url, headers=HEADERS, data=data)
    return r.json()


def post_from_csv(csv_file:str):
    with open(csv_file,"r") as f:
        dr = DictReader(f)
        for i in dr:
            r = post_request(i,url_post)
            print(r)


def post_from_json_file(json_file:str):
    with open(json_file) as f:
        record_list_raw = f.readlines()
        for i in record_list_raw:
            try:
                cleaned = literal_eval(i)
                r = post_request(cleaned,url_post)
                print(r)
            except:
                continue


post_from_csv("gold.csv")
