import requests

headerdata = {
'accept': 'text/plain'
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/3",headers=headerdata)

print(response.json())
print(response.status_code)

assert response.status_code == 200