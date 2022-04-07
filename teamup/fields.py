from collections import namedtuple

from teamup.constants import LOCATIONS, PARKS

Field = namedtuple('Field', ('id', 'calendar', 'name', 'location'))


def get_fields(subcals):
    fields = {}
    for loc in LOCATIONS:
        field_id = subcals.get_subcal_id(loc)
        fields[field_id] = Field(
            subcals.get_subcal_id(loc),
            loc,
            PARKS[loc],
            LOCATIONS[loc]
        )
    return fields


def get_field_id(event, fields):
    return [c for c in event.get_calendars() if c in fields.keys()][0]


def get_field_info(event, fields):
    return fields[get_field_id(event, fields)]
