import pickle
import datetime

import teamup


FILE = f'backups/cal-backup-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.p'
START = '2023-03-01'
END = '2023-07-31'


def backup():
    print('Pulling events...')
    events = teamup.get_events(START, END)
    with open(FILE, 'wb') as fp:
        pickle.dump(events, fp)
    print(f'Events successfully written to {FILE}')


if __name__ == '__main__':
    backup()
