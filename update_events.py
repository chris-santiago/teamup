import teamup

START = '2022-03-01'
END = '2022-07-31'

cals = teamup.get_subcals()
events = teamup.get_events(START, END)
fields = teamup.get_fields(cals)


if __name__ == '__main__':
    updater = teamup.Updater(events, fields, cals)
    updater.update_parks()
    # updater.update_coach_details()  # todo leaving this out as we may not want contact info on share calendar app
    updater.run()
