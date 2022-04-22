import teamup

START = '2022-03-01'
END = '2022-07-31'
DIVISIONS = ['majors', 'minors', 'juniors']

cals = teamup.get_subcals()
events = teamup.get_events(START, END)
fields = teamup.get_fields(cals)

schedules = {}
for d in DIVISIONS:
    schedules[d] = teamup.DivisionSchedule(d, events, cals, START, END)

if __name__ == '__main__':
    for k, s in schedules.items():
        s.to_csv(f'~/Dropbox/QA Baseball/{k}-schedule.csv')
