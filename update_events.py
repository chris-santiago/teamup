import teamup

START = '2022-03-01'
END = '2022-07-31'

cals = teamup.get_subcals()
events = teamup.get_events(START, END)
fields = teamup.get_fields(cals)


if __name__ == '__main__':
    updater = teamup.Updater(events, fields)
    updater.update_parks()
    updater.run()
