import requests
from flask import jsonify
from flask_login import login_required, current_user

from app import app
from app.utils import get_buy_rate, API_PB


@app.route('/')
def index():
    return jsonify(heartbeat='ok')


@app.route('/btcRate')
@login_required
def btc_rate():
    pb_rate_xml = requests.get(API_PB)
    btc_uah_rate = get_buy_rate(pb_rate_xml, 'BTC')
    return jsonify(auth_user=current_user.email, btc_rate=round(float(btc_uah_rate), 2))
