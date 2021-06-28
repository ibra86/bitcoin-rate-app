import json
import xml.etree.ElementTree as ET
from dataclasses import asdict

from app.users import User

USERS_FILE = 'users.jsonl'


def get_users_all():
    users_all = {}
    with open(USERS_FILE, 'r') as f:
        for line in f:
            line_d = json.loads(line)
            users_all[line_d.get('email')] = line_d
    return users_all


def get_user_from_storage(email):
    users_all = get_users_all()
    try:
        user = User(**users_all[email])
        return user
    except:  # noqa
        pass


def put_user_to_storage(email, password_hsh):
    user = User(email, password_hsh)
    json.dumps(asdict(user))
    with open(USERS_FILE, 'a') as f:
        f.write(json.dumps(asdict(user)) + "\n")


def get_buy_rate(pb_rate_xml, ccy):
    root = ET.fromstring(pb_rate_xml.text)
    for element in root:
        for e in element:
            if e.attrib.get('ccy') == ccy:
                return e.attrib.get('buy')
