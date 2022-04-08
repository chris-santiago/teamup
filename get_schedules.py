import teamup

START = '2022-03-01'
END = '2022-07-31'

cals = teamup.get_subcals()
events = teamup.get_events(START, END)
fields = teamup.get_fields(cals)
majors = teamup.DivisionSchedule('majors', events, cals, START, END)
minors = teamup.DivisionSchedule('minors', events, cals, START, END)


if __name__ == '__main__':
    majors.to_csv('~/Dropbox/QA Baseball/majors-schedule.csv')
    minors.to_csv('~/Dropbox/QA Baseball/minors-schedule.csv')
