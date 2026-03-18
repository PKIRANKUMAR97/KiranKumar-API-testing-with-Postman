import requests

headerdata = {
'accept': 'text/plain'
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/3",headers=headerdata)
print("Before PUT http call")
print(response.json())

headersdataPUT = {
'accept': 'text/plain',
    'content-type': 'application/json'
}
PUTpayload={
  "id": 333,
  "title": "Updated Title after PUT",
  "dueDate": "2026-03-18T18:22:19.444Z",
  "completed": True
}

responsePUT = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/3",
                           headers=headerdata,
                           json = PUTpayload
                           )

print("After PUT http call")
print(responsePUT.json())