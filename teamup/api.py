import requests

from teamup.constants import BASE, HEADERS


def check_access():
    resp = requests.get(
        url=f'{BASE}/check-access',
        headers=HEADERS
    )
    if resp.status_code == 200:
        print('Access OK')
    else:
        print('No access')
