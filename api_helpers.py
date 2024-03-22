import requests
import logging
import json

# base_url = 'http://localhost:5000'
base_url = 'http://127.0.0.1:5000'

# GET requests
def get_api_data(endpoint, params = {}):
    response = requests.get(f'{base_url}{endpoint}', params=params)
    return response

# POST requests
def post_api_data(endpoint, data):
    response = requests.post(f'{base_url}{endpoint}', json=data)
    return response

# PATCH requests
def patch_api_data(endpoint, data):
    headers = {'Content-Type': 'application/json'}
    assert 'Content-Type' in headers
    assert headers['Content-Type'] == 'application/json'
    assert isinstance(data, dict)

    # Print debug information
    print("Request:", f'{base_url}{endpoint}', headers, data)

    response = requests.patch(f'{base_url}{endpoint}', headers=headers, json=data)
    return response