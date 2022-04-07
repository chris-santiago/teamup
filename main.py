import asyncio

import aiohttp

import teamup

START = '2022-03-01'
END = '2022-07-31'

cals = teamup.get_subcals()
events = teamup.get_events(START, END)
fields = teamup.get_fields(cals)


updater = teamup.Updater(events, fields)

# # Setting up for async.
# # Updating Field Name by mapping subcalendar IDs to calendar names, fields, locations, etc.
# updates = []
# for e in events:
#     park = teamup.get_field_info(e, fields)
#     e.set_park(park.name)
#     updates.append(teamup.create_update(e.id, e.info))
#
#
# # Setting up for async.
# # Updating Field Number by extracting from calendar name
# updates = []
# for e in events:
#     park = teamup.get_field_info(e, fields)
#     field_num = teamup.extract_field_num(park)
#     e.set_field(field_num)
#     updates.append(teamup.create_update(e.id, e.info))
#
#
# # Setting up for async.
# # Updating loation
# updates = []
# for e in events:
#     park = teamup.get_field_info(e, fields)
#     e.set_loc(park.location)
#     updates.append(teamup.create_update(e.id, e.info))

# Running above in loops and not in functions ensures that updates are additive.

# # Asynchronous Routines --------------------
# async def async_put(session, update):
#     async with session.put(url=update.url, headers=update.headers, json=update.data) as response:
#         return await response.text()
#
#
# async def async_put_all(updates):
#     connector = aiohttp.TCPConnector(limit_per_host=5, limit=500)
#     async with aiohttp.ClientSession(connector=connector) as session:
#         results = await asyncio.gather(
#             *[async_put(session, update) for update in updates],
#             return_exceptions=False
#         )
#         return results
#
#
# def run(event_updates):
#     res = asyncio.run(async_put_all(event_updates))


# #  just play --------------
# braves = teamup.find_events('Braves', START, END)
# teamup.get_team_schedule('Braves', cals, START, END)
# teamup.get_field_info(braves[0], fields)
# #  just play --------------


# if __name__ == '__main__':
#     # run(updates)
