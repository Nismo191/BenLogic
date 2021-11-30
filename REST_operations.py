import requests

def get(url, auth=None, params=None, headers=None):
    return requests.get(url, auth=auth, params=params, headers=headers).json()

def post(url, data=None, auth=None,  params=None, headers=None):
    return requests.post(url, json=data).json()