import json

import requests

headers_data={
    'Content-Type': 'application/json'
}

json_file=open('./users.json')
json_payload=json.load(json_file)


base_url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

response_body = requests.post(url=base_url, headers=headers_data,json=json_payload)
print(response_body.json())
print(response_body.status_code)

assert response_body.status_code == 200