import pandas as pd

import teamup

START = '2022-03-01'
END = '2022-07-31'
DIVISIONS = ['teeball', 'coach pitch', 'minors', 'majors', 'juniors', 'seniors', '11u', '12u']

cals = teamup.get_subcals()
events = teamup.get_events(START, END)
fields = teamup.get_fields(cals)

schedules = {}
for d in DIVISIONS:
    schedules[d] = teamup.DivisionSchedule(d, events, cals, START, END)

if __name__ == '__main__':
    for k, s in schedules.items():
        s.to_csv(f'~/Dropbox/QA Baseball/{k}-schedule.csv')

    with pd.ExcelWriter('~/Dropbox/QA Baseball/all-schedules.xlsx') as writer:
        for k, s in schedules.items():
            sched = teamup.add_coach_info(s.to_pandas(), teamup.COACHES)
            sched.to_excel(writer, sheet_name=k, index=False)
