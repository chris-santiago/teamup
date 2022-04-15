import re

from teamup.fields import get_fields, get_field_info
from teamup.events import find_events
from teamup.coaches import COACHES


def get_team_schedule(team, subcals, start, end):
    fields = get_fields(subcals)
    team_events = find_events(team, start, end)
    return [
        (e.get_title(), e.get_date()[0], get_field_info(e, fields).name, e.get_loc())
        for e in team_events
    ]


def worton_handler(park):
    if '-B/C/D' in park.calendar:
        return 'See diamond board front of park, day of.'
    if '-AA' in park.calendar:
        return 'AA'
    return ''


def extract_field_num(park):
    if 'Worton' in park.calendar:
        return worton_handler(park)
    match = re.search('\d', park.calendar)
    if match:
        return match.group()
    return '1'  # default for single-field parks


def get_coach_details(team):
    return '\n'.join([team] + [f'{k}: {v}' for k, v in COACHES[team].items()])
