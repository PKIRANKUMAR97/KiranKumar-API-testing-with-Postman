import requests

headerdata = {
'accept': 'text/plain',
'Content-Type': 'application/json',
}

request_payload ={
  "id": 908,
  "title": "SDETHA",
  "dueDate": "2026-03-18T17:52:04.292Z",
  "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",
                        headers=headerdata,
                        json=request_payload)

print(response.json())
print(response.status_code)
jsonoutputData = response.json()
assert response.status_code == 200
assert jsonoutputData['id'] == 908
assert jsonoutputData["title"] == "SDETHA"


