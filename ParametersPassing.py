import requests


parameters_to_pass = {
    "page":1,
    "per_page":2
}

url = "https://gorest.co.in/public/v2/users"

response_output = requests.get(url , params=parameters_to_pass)
print(response_output.json())
assert response_output.status_code == 200