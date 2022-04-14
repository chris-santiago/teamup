import asyncio
import re

import aiohttp

from teamup.fields import get_field_info
from teamup.misc import extract_field_num, get_coach_details
from teamup.coaches import COACHES


class Updater:
    def __init__(self, events, fields, cals):
        self.events = events
        self.fields = fields
        self.cals = cals

    def update_parks(self):
        for e in self.events:
            if e.subcal_id in [10719330, 10703990]:  # Don't change Denton/Caroline park info  # todo temporary
                continue
            park = get_field_info(e, self.fields)
            field_num = extract_field_num(park)
            e.set_park(park.name)
            e.set_field(field_num)
            e.set_loc(park.location)

    def update_coach_details(self):
        for e in self.events:
            teams = [c for c in e.get_calendars() if 'Teams' in self.cals.get_subcal_name(c)]
            details = []
            for ID in teams:
                cal_name = self.cals.get_subcal_name(ID)
                team_name = re.findall(r"(?=(" + '|'.join(list(COACHES.keys())) + r"))", cal_name)
                try:
                    details.append(get_coach_details(team_name[0]))
                except IndexError:
                    print(f'No details for subcal: {cal_name}')
            e.set_attr('notes', '\n'.join(details))

    def run(self):
        async def async_put(session, update):
            async with session.put(url=update.url, headers=update.headers,
                                   json=update.data) as response:
                return await response.text()

        async def async_put_all(updates):
            connector = aiohttp.TCPConnector(limit_per_host=5, limit=500)
            async with aiohttp.ClientSession(connector=connector) as session:
                results = await asyncio.gather(
                    *[async_put(session, update) for update in updates],
                    return_exceptions=False
                )
                return results

        event_updates = [e.get_update_params() for e in self.events]
        res = asyncio.run(async_put_all(event_updates))