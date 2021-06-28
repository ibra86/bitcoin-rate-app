import json


def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.json['heartbeat'] == 'ok'


def test_btc_rate(client):
    client.post('/user/login',
                data=json.dumps({'email': 'test', 'password': 'test'}),
                content_type='application/json')

    res = client.get('/btcRate')
    assert res.status_code == 200
    assert res.json['auth_user'] == 'test'
    assert res.json['btc_rate']
    isinstance(res.json['btc_rate'], float)
