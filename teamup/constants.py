import configparser
import pathlib


def get_config(section='DEFAULT'):
    home = pathlib.Path('~').expanduser()
    fp = home.joinpath('teamup.cfg')
    config = configparser.ConfigParser()
    config.read(fp)
    return config[section]


CONFIG = get_config()
KEY = CONFIG['key']
CAL_KEY = CONFIG['cal_key']
CAL_PASS = CONFIG['cal_pass']

BASE = 'https://api.teamup.com'
BASE_URL = f'{BASE}/{CAL_KEY}'
HEADERS = {
    'Teamup-Token': CONFIG['key'],
    'Teamup-Password': CONFIG['cal_pass']
}

LOCATIONS = {
    'Away > Chestertown': '10932 Worton Road, Worton, MD 21678',
    'Away > Denton': 'Lions Park, Denton, MD 21629',
    'Away > Galena': '13753 Augustine Herman Hwy, Galena, MD 21635',
    'Away > Millington': '10601 Galena Rd. Millington, MD 21651',
    'Away > North Caroline': 'Lions Park, Denton, MD 21629',
    'Away > Worton': '10932 Worton Road, Worton, MD 21678',
    'CES': '213 Homewood Ave, Centreville, MD 21617',
    'Church Hill > CH-1': '1130 Sudlersville Rd, Church Hill, MD 21623',
    'Church Hill > CH-2': '1130 Sudlersville Rd, Church Hill, MD 21623',
    'CMS > CMS-1': '231 Ruthsburg Rd, Centreville, MD 21617',
    'CMS > CMS-2': '231 Ruthsburg Rd, Centreville, MD 21617',
    'CMS > CMS-3': '231 Ruthsburg Rd, Centreville, MD 21617',
    'CMS > CMS-4': '231 Ruthsburg Rd, Centreville, MD 21617',
    'Roosevelt Park > RP-1': 'Morgan St, Queen Anne, MD 21657',
    'Route 18 > RT18-4': '1945 4-H Park Road, Centreville, MD 12617',
    'White Marsh > WM-1': '200 Bloomfield Farm Ln, Centreville, MD 21617',
    'White Marsh > WM-2': '200 Bloomfield Farm Ln, Centreville, MD 21617',
    'White Marsh > WM-3': '200 Bloomfield Farm Ln, Centreville, MD 21617',
    'White Marsh > WM-4': '200 Bloomfield Farm Ln, Centreville, MD 21617',
}

PARKS = {
    'Away > Chestertown': 'Worton Park',
    'Away > Denton': 'Lions Park',
    'Away > Galena': 'Toal Park',
    'Away > Millington': 'Lions Field',
    'Away > North Caroline': 'Lions Park',
    'Away > Worton': 'Worton Park',
    'CES': 'Centreville Elementary School',
    'Church Hill > CH-1': 'Church Hill Park',
    'Church Hill > CH-2': 'Church Hill Park',
    'CMS > CMS-1': 'Centreville Middle School',
    'CMS > CMS-2': 'Centreville Middle School',
    'CMS > CMS-3': 'Centreville Middle School',
    'CMS > CMS-4': 'Centreville Middle School',
    'Roosevelt Park > RP-1': 'Roosevelt Park',
    'Route 18 > RT18-4': 'Route 19 Park',
    'White Marsh > WM-1': 'White Marsh Park',
    'White Marsh > WM-2': 'White Marsh Park',
    'White Marsh > WM-3': 'White Marsh Park',
    'White Marsh > WM-4': 'White Marsh Park',
}

COACHES = {'Flying Squirrels': {'Head Coach': 'Josh Dishong',
                                'Phone': '443-235-2267',
                                'Email': 'joshua.dishong@qacps.org'},
           'River Dogs': {'Head Coach': 'Mike Grasso',
                          'Phone': '410-725-8330',
                          'Email': 'mjgrasso1989@hotmail.com'},
           'Blue Claws': {'Head Coach': 'Kyle Hastings',
                          'Phone': '973-769-2707',
                          'Email': 'kwhastings@gmail.com'},
           'Fireflies': {'Head Coach': 'Garrett  Johnson ',
                         'Phone': '410-310-8152',
                         'Email': 'gmjohnson10687@hotmail.com'},
           'Shorebirds': {'Head Coach': 'Rachel Lloyd',
                          'Phone': '410-490-5829',
                          'Email': 'rmlloyd2011@gmail.com'},
           'Sea Wolves': {'Head Coach': 'Melanie Connelly',
                          'Phone': '443-623-4325',
                          'Email': 'mconnelly7832@gmail.com'},
           'Knights': {'Head Coach': 'Brandon Morris ',
                       'Phone': '410-725-6723',
                       'Email': 'branmor1993@gmail.com'},
           'Intimidators': {'Head Coach': 'Sean Smith',
                            'Phone': '410-507-1899',
                            'Email': 'adsmith172527@gmail.com'},
           'Hammerheads': {'Head Coach': 'Leandra Thorpe',
                           'Phone': '520-360-5443',
                           'Email': 'leandra.espinosa@yahoo.com'},
           'Louisville Bats': {'Head Coach': 'Skip Ward',
                               'Phone': '410-507-8963',
                               'Email': 'skipw106@aol.com'},
           'Dragons': {'Head Coach': 'Trey Carlson',
                       'Phone': '410-490-0429',
                       'Email': 'sassyforever485@gmail.com'},
           'Redwings': {'Head Coach': 'Kellen Shepard',
                        'Phone': '410-739-7487',
                        'Email': 'kshepard@baybeachclub.com'},
           'Dust Devils': {'Head Coach': 'Cailean Leith',
                           'Phone': '410-897-2129',
                           'Email': 'leithal34@gmail.com'},
           'Jumbo Shrimp': {'Head Coach': 'Brad Dutton',
                            'Phone': '412-554-9680',
                            'Email': 'brad.b.dutton@gmail.com'},
           'Cannon Ballers': {'Head Coach': 'Ryan Devlin',
                              'Phone': '973-600-2998',
                              'Email': 'rdevlin1@gmail.com'},
           'Baysox': {'Head Coach': 'Jeremy Furrow',
                      'Phone': '443-623-4142',
                      'Email': 'furrow_95@yahoo.com'},
           'Space Cowboys': {'Head Coach': 'Jesse Hicks',
                             'Phone': '203-240-5135',
                             'Email': 'jessehicks26@gmail.com'},
           'Reading Phillies': {'Head Coach': 'Matt Moore',
                                'Phone': '443-262-1924',
                                'Email': 'mmoore081382@gmail.com'},
           'Threshers': {'Head Coach': 'Michael  Mayer',
                         'Phone': '215-375-2527',
                         'Email': 'cbreds27@aol.com'},
           'Rough Riders': {'Head Coach': 'Buddy Custer',
                            'Phone': '443-433-6220',
                            'Email': 'bcuster@uqalions.org'},
           'Rangers': {'Head Coach': 'Skip Ward',
                       'Phone': '410-507-8963',
                       'Email': 'skipw106@aol.com'},
           'Nationals': {'Head Coach': 'Chris Kennedy',
                         'Phone': '443-618-7295',
                         'Email': 'kennedy8250@gmail.com'},
           'Athletics': {'Head Coach': 'Mike Schoonmaker',
                         'Phone': '301-787-3299',
                         'Email': 'mikeschoonmaker@hotmail.com'},
           'Pirates': {'Head Coach': 'Jerry Gott',
                       'Phone': '410-310-7588',
                       'Email': 'gerald.gott12@gmail.com'},
           'Braves': {'Head Coach': 'Robbie Lisle',
                      'Phone': '443-463-3974',
                      'Email': 'rlisle105@gmail.com'},
           'Orioles': {'Head Coach': 'Tom McAndrews',
                       'Phone': '410-725-3868',
                       'Email': 'ghtigers69@gmail.com'},
           'Dodgers': {'Head Coach': 'Ryan Fleetwood',
                       'Phone': '410-430-6642',
                       'Email': 'ryandf@gmail.com'},
           'TBD': {'Head Coach': 'Joe Jordan',
                   'Phone': '443-988-2466',
                   'Email': 'doublej3037@yahoo.com'}}
