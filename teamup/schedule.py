import pandas as pd

from teamup.coaches import COACHES


class DivisionSchedule:
    div_map = {
        'teeball': 'TB',
        'coach pitch': 'CP',
        'majors': 'MJ',
        'minors': 'MN',
        'seniors': 'Seniors',
        'juniors': 'Juniors'
    }

    def __init__(self, division, events, calendars, start, end):
        self.div_name = division.lower()
        self.div_code = self.div_map[self.div_name]
        self.events = events
        self.cals = calendars
        self.start = start
        self.end = end

    def __repr__(self):
        return f"DivisionSchedule(division='{self.div_name}', start='{self.start}', end={self.end}')"

    def get_league_cal_ids(self):  # only useful if away teams have their own calendars
        return [v for k, v in self.cals.cals_by_name().items() if self.div_code in k]

    def get_teams(self):
        return [c.split(' ')[-2] for c in self.cals.names if self.div_code in c]

    def get(self):
        return [e for e in self.events
                if any(team in e.title for team in self.get_teams())
                and '@' in e.title]

    def to_pandas(self):
        schedule = pd.DataFrame([
            {
                'Game': g.title,
                'Date': g.date,
                'Visitor': split_visitor_home(g.title)[0],
                'Home': split_visitor_home(g.title)[1],
                'Park': g.park,
                'Field': g.get_field(),
                'Location': g.get_loc()
            }
            for g in self.get()
        ])
        return schedule

    def to_csv(self, filename):
        add_coach_info(self.to_pandas(), COACHES).to_csv(filename, index=False)


def split_visitor_home(title):
    teams = title.split('@')
    away = teams[0].strip()
    home = teams[1].strip()
    return away, home


def add_coach_info(df, coaches):
    for team in ['Visitor', 'Home']:
        df[f'{team} Coach Info'] = [coaches.get(x, {}) for x in df[team]]
        df[f'{team} Coach Name'] = df[f'{team} Coach Info'].apply(lambda x: x.get('Head Coach'))
        df[f'{team} Coach Phone'] = df[f'{team} Coach Info'].apply(lambda x: x.get('Phone'))
        df[f'{team} Coach Email'] = df[f'{team} Coach Info'].apply(lambda x: x.get('Email'))
        df.drop(f'{team} Coach Info', axis=1, inplace=True)
    return df
