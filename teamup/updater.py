import asyncio

import aiohttp

from teamup.fields import get_field_info
from teamup.misc import extract_field_num


class Updater:
    def __init__(self, events, fields):
        self.events = events
        self.fields = fields

    def update_parks(self):
        for e in self.events:
            park = get_field_info(e, self.fields)
            field_num = extract_field_num(park)
            e.set_park(park.name)
            e.set_field(field_num)
            e.set_loc(park.location)

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