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


def extract_field_num(park):
    match = re.search('\d', park.calendar)
    if match:
        return match.group()
    return ''


def get_coach_details(team):
    return '\n'.join([team] + [f'{k}: {v}' for k, v in COACHES[team].items()])
