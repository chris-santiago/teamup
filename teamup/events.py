import datetime
import copy
from collections import namedtuple

import requests

from teamup.constants import BASE_URL, HEADERS, KEY, CAL_PASS

Update = namedtuple('Update', ('url', 'headers', 'data'))

RECURRING = 'all'


class Event:
    def __init__(self, event):
        self._original = copy.deepcopy(event)
        self.info = self.add_custom_if_missing(event)
        self.id = self.info['id']
        self.subcal_id = self.info['subcalendar_id']
        self.title = self.info['title']
        self.date = self.info['start_dt'][:10]
        self.park = self.info['custom'].get('park')

    def __repr__(self):
        return f"Event(title='{self.title}', date='{self.date}', id={self.id}, subcal_id={self.subcal_id}')"

    @staticmethod
    def add_custom_if_missing(event):
        if event.get('custom') is None:
            event['custom'] = {}
        return event

    @property
    def tz(self):
        iso = datetime.datetime.fromisoformat(self._original['start_dt'])
        return iso.tzinfo

    def revert(self):
        self.info = self._original.copy()

    def get_title(self):
        return self.info['title']

    def set_title(self, title):
        self.info['title'] = title

    def get_loc(self):
        return self.info['location']

    def set_loc(self, location):
        self.info['location'] = location

    def get_calendars(self):
        return self.info['subcalendar_ids']

    def add_calendar(self, subcal_id):
        self.info['subcalendar_ids'].append(subcal_id)

    def remove_calendar(self, subcal_id):
        self.info['subcalendar_ids'].remove(subcal_id)

    def get_date(self):
        return self.info['start_dt'], self.info['end_dt']

    def set_date(self, year, month, day, hour, minute, offset=2):
        start = datetime.datetime(year, month, day, hour, minute, tzinfo=self.tz)
        duration = datetime.timedelta(hours=offset)
        end = start + duration
        self.info['start_dt'] = start.isoformat()
        self.info['end_dt'] = end.isoformat()

    def get_field(self):
        return self.info['custom'].get('field')

    def set_field(self, field):
        self.info['custom'].update({'field': field})

    def get_park(self):
        return self.info['custom'].get('park')

    def set_park(self, park):
        self.info['custom'].update({'park': park})

    def get_attr(self, attr):
        return self.info[attr]

    def set_attr(self, attr, value):
        self.info[attr] = value

    def update(self, recurring='all'):  # todo I don't think this is use anymore after switch to aiohttp
        if recurring not in ['all', 'single', 'future']:
            raise ValueError("Recurring must be in `{'all', 'single', 'future'}`")
        self.info['redit'] = recurring
        params = self.get_update_params()
        resp = requests.put(url=params.url, headers=params.headers, json=params.data)
        print(resp.status_code)

    def get_update_params(self):
        headers = {
            'Teamup-Token': KEY,
            'Content-type': 'application/json',
            'Teamup-Password': CAL_PASS
        }
        self.info['redit'] = RECURRING
        return Update(url=f'{BASE_URL}/events/{self.id}', headers=headers, data=self.info)


def get_events(start=None, end=None):
    if not start and not end:
        resp = requests.get(
            url=f'{BASE_URL}/events',
            headers=HEADERS
        )
    else:
        resp = requests.get(
            url=f'{BASE_URL}/events?startDate={start}&endDate={end}',
            headers=HEADERS
        )
    return [Event(e) for e in resp.json()['events']]


def find_events(query=None, start=None, end=None, subcal_id=None):
    endpoint = f'{BASE_URL}/events?query={query}'
    if not subcal_id:
        if not start and not end:
            resp = requests.get(
                url=endpoint,
                headers=HEADERS
            )
        else:
            resp = requests.get(
                url=f'{endpoint}&startDate={start}&endDate={end}',
                headers=HEADERS
            )
    else:
        if not start and not end:
            resp = requests.get(
                url=f'{endpoint}&subcalendarId[]={subcal_id}',
                headers=HEADERS
            )
        else:
            resp = requests.get(
                url=f'{endpoint}&startDate={start}&endDate={end}&subcalendarId[]={subcal_id}',
                headers=HEADERS
            )
    return [Event(e) for e in resp.json()['events']]


def get_event(event_id):
    resp = requests.get(
        url=f'{BASE_URL}/events/{event_id}',
        headers=HEADERS
    )
    return resp.json()


def get_event_history(event_id):
    resp = requests.get(
        url=f'{BASE_URL}/events/{event_id}/history',
        headers=HEADERS
    )
    return resp.json()
