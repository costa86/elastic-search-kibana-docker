from typing import List
import requests
import json
from pprint import pprint
from csv import DictReader
from ast import literal_eval


base_url = "http://localhost:9200"
data_stream = "nyc"
results_qtd = 20

url_get = f"{base_url}/{data_stream}/_search"
url_post = f"{base_url}/{data_stream}/_doc"
url_put = f"{base_url}/{data_stream}/_bulk"


json_get = {"size":results_qtd,"query": {"match": {"Category": "Asian"}}}
json_get_all = {"query": {"match_all": {}}}

json_post = {"name": "ana", "age": 50}
json_put = [{"name": "carla"}, {"name": "sara"}]


def get_request(json_data: dict, url):
    headers = {"Content-Type": "application/json"}
    r = requests.get(url=url, headers=headers, data=json.dumps(json_data))
    return r.json()


def post_request(json_data: dict, url):
    headers = {"Content-Type": "application/json"}
    r = requests.post(url=url, headers=headers, data=json.dumps(json_data))
    return r.json()


def put_request(json_list: List[dict], url):
    headers = {"Content-Type": "application/json"}
    final_list = []

    for i in json_list:
        final_list.append({"create": {}})
        final_list.append(i)

    data = '\n'.join([json.dumps(i) for i in final_list]) + '\n'
    r = requests.put(url=url, headers=headers, data=data)
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

# # a = put_request(json_put, url_put)
# a = get_request(json_get_all, url_get)
# a = len(a)
post_from_csv("nyc.csv")
# pprint(a)
# post_from_json_file("log/log.log")