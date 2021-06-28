import requests
from flask import jsonify
from flask_login import login_required, current_user

from app import app
from app.utils import get_buy_rate


@app.route('/')
def index():
    return jsonify(heartbeat='ok')


@app.route('/btcRate')
@login_required
def btc_rate():
    api_pb = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
    pb_rate_xml = requests.get(api_pb)
    btc_uah_rate = get_buy_rate(pb_rate_xml, 'BTC')
    return jsonify(auth_user=current_user.email, btc_rate=round(float(btc_uah_rate), 2))
