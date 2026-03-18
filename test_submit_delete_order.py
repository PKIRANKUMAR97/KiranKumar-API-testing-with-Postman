import requests
import json

class TestOrderAPI:
    BASE_URL ="https://simple-books-api.glitch.me/orders"
    AUTH_TOKEN = "c0b4226fc55092609d5930e6b2f40b0b4d91cd1d0f8dcbeb737d9013f6a425d1"
    def test_submit_delete_order(self):
        requests.post(self.BASE_URL)
