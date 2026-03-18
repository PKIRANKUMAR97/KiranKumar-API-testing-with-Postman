import requests
headerdata = {
'accept': 'text/plain',
'Content-Type': 'application/json',
'Authorization': 'Bearer ca8d3d5da96881ad59e2e44d3b8a479c0b30a72d6086ac95eaf42eb1fe384cf7'
}

request_payload ={"id":9090,
                  "name":"Harsit Rana",
                  "email":"viratkohli16@virat.com",
                  "gender":"female",
                  "status":"active"}

url = "https://gorest.co.in/public/v2/users"
response = requests.post( url, headers=headerdata, json=request_payload)
print(response.json())

assert response.status_code == 201

GETresponse = requests.get(url+'/'+str(response.json()['id']), headers=headerdata)
print(GETresponse.json())
assert GETresponse.status_code == 200