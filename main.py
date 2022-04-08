import teamup

START = '2022-03-01'
END = '2022-07-31'

cals = teamup.get_subcals()
events = teamup.get_events(START, END)
fields = teamup.get_fields(cals)


# #  just play --------------
# braves = teamup.find_events('Braves', START, END)
# teamup.get_team_schedule('Braves', cals, START, END)
# teamup.get_field_info(braves[0], fields)
# #  just play --------------


if __name__ == '__main__':
    updater = teamup.Updater(events, fields)
    updater.update_parks()
    updater.run()
