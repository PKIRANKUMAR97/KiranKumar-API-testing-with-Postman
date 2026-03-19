import pytest
import requests

def test_api_pytest_get_validation():
    header_data = {'Content-Type': 'application/json'}
    base_url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

    response_body = requests.get(url=str(base_url)+'/2', headers=header_data)
    print(response_body.json())
    assert response_body.status_code == 200

