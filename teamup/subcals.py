import requests

from teamup.constants import BASE_URL, HEADERS


def get_subcals():
    resp = requests.get(
        url=f'{BASE_URL}/subcalendars',
        headers=HEADERS
    )
    return Subcalendars(resp.json()['subcalendars'])


def get_team_names(subcalendar):
    return [x for x in subcalendar.names if 'Teams' in x]


class Subcalendars:
    def __init__(self, cals):
        self.cals = cals

    def cals_by_name(self):
        return {c['name']: c['id'] for c in self.cals}

    def cals_by_id(self):
        return {c['id']: c['name'] for c in self.cals}

    def get_subcal_id(self, name):
        return self.cals_by_name()[name]

    def get_subcal_name(self, ID):
        return self.cals_by_id()[ID]

    @property
    def names(self):
        return [c['name'] for c in self.cals]
