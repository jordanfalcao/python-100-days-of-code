import os
import requests

SHEET_API = os.environ['SHEET_API']
BEARER = os.environ['BEARER']


def post_new_row(first_name, last_name, email):
    endpoint = f"{SHEET_API}"
    headers = {
        "Authorization": f"Bearer {BEARER}"
    }

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    response = requests.post(url=endpoint, json=body, headers=headers)
    response.raise_for_status()
    print(response.text)