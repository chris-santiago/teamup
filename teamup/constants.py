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
    'Away > Caroline > Denton Lions Club-1': 'Lions Park, Denton, MD 21629',
    'Away > Caroline > Greensboro Lions Club-2': 'Greensboro Lions Park, Greensboro, MD 21639',
    'Away > Caroline > Martin Sutton Park-1': '302 W. 4th Street, Ridgely, MD 21660',
    'Away > Kent > Worton-AA': '10932 Worton Road, Worton, MD 21678',
    'Away > Kent > Worton-B/C/D': '10932 Worton Road, Worton, MD 21678',
    'Away > Kent > Toal Park': '13753 Augustine Herman Hwy, Galena, MD 21635',
    'Away > Kent > Millington': '10601 Galena Rd. Millington, MD 21651',
    'CES': '213 Homewood Ave, Centreville, MD 21617',
    'Church Hill > CH-1': '1130 Sudlersville Rd, Church Hill, MD 21623',
    'Church Hill > CH-2': '1130 Sudlersville Rd, Church Hill, MD 21623',
    'CMS > CMS-1': '231 Ruthsburg Rd, Centreville, MD 21617',
    'CMS > CMS-2': '231 Ruthsburg Rd, Centreville, MD 21617',
    'CMS > CMS-3': '231 Ruthsburg Rd, Centreville, MD 21617',
    'CMS > CMS-4': '231 Ruthsburg Rd, Centreville, MD 21617',
    'Roosevelt Park > RP-1': 'Morgan St, Queen Anne, MD 21657',
    'Route 18 > RT18-1': '1945 4-H Park Road, Centreville, MD 12617',
    'Route 18 > RT18-2': '1945 4-H Park Road, Centreville, MD 12617',
    'Route 18 > RT18-3': '1945 4-H Park Road, Centreville, MD 12617',
    'Route 18 > RT18-4': '1945 4-H Park Road, Centreville, MD 12617',
    'White Marsh > WM-1': '200 Bloomfield Farm Ln, Centreville, MD 21617',
    'White Marsh > WM-2': '200 Bloomfield Farm Ln, Centreville, MD 21617',
    'White Marsh > WM-3': '200 Bloomfield Farm Ln, Centreville, MD 21617',
    'White Marsh > WM-4': '200 Bloomfield Farm Ln, Centreville, MD 21617',
}

PARKS = {
    'Away > Caroline > Denton Lions Club-1': 'Denton Lions Park',
    'Away > Caroline > Greensboro Lions Club-2': 'Greensboro Lions Park',
    'Away > Caroline > Martin Sutton Park-1': 'Martin Sutton Park',
    'Away > Kent > Worton-AA': 'Worton Park',
    'Away > Kent > Worton-B/C/D': 'Worton Park',
    'Away > Kent > Toal Park': 'Toal Park',
    'Away > Kent > Millington': 'Lions Field',
    'CES': 'Centreville Elementary School',
    'Church Hill > CH-1': 'Church Hill Park',
    'Church Hill > CH-2': 'Church Hill Park',
    'CMS > CMS-1': 'Centreville Middle School',
    'CMS > CMS-2': 'Centreville Middle School',
    'CMS > CMS-3': 'Centreville Middle School',
    'CMS > CMS-4': 'Centreville Middle School',
    'Roosevelt Park > RP-1': 'Roosevelt Park',
    'Route 18 > RT18-1': 'Route 18 Park',
    'Route 18 > RT18-2': 'Route 18 Park',
    'Route 18 > RT18-3': 'Route 18 Park',
    'Route 18 > RT18-4': 'Route 18 Park',
    'White Marsh > WM-1': 'White Marsh Park',
    'White Marsh > WM-2': 'White Marsh Park',
    'White Marsh > WM-3': 'White Marsh Park',
    'White Marsh > WM-4': 'White Marsh Park',
}
