import tqdm

updates = []
events = Events('2022-03-01', '2022-07-31')
for e in tqdm.tqdm(events.all):
    calendars = [sc.get_subcal_name(x) for x in e['subcalendar_ids']]
    for c in calendars:
        if c in LOCATIONS.keys():
            update_location = LOCATIONS[c]
            e['location'] = update_location
            e['redit'] = 'all'
            updates.append(e)
            # update_event(e['id'], e)


events = find_events('Braves', '2022-03-01', '2022-07-31')