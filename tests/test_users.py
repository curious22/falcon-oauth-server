import requests
from tests import fixtures


BASE_URL = 'http://0.0.0.0:5000/v1/users'


def test_create_witout_params():
    resp = requests.post(url=BASE_URL)
    json_resp = resp.json()

    assert resp.status_code == 400
    assert json_resp['meta']['message'] == 'Invalid Parameter'


# ----- Password -----
def test_create_witout_pass():
    resp = requests.post(url=BASE_URL, json=fixtures.params_without_pass)
    json_resp = resp.json()

    assert resp.status_code == 400
    assert 'password' in json_resp['meta']['description']


def test_create_minlength_pass():
    resp = requests.post(url=BASE_URL, json=fixtures.minlength_pass)
    json_resp = resp.json()

    assert resp.status_code == 400
    assert 'min length is 8' in json_resp['meta']['description']['password']


def test_create_maxlength_pass():
    resp = requests.post(url=BASE_URL, json=fixtures.maxlength_pass)
    json_resp = resp.json()

    assert resp.status_code == 400
    assert 'max length is 64' in json_resp['meta']['description']['password']


# ----- Username -----
def test_create_witout_username():
    resp = requests.post(url=BASE_URL, json=fixtures.params_without_username)
    json_resp = resp.json()

    assert resp.status_code == 400
    assert 'username' in json_resp['meta']['description']


def test_create_minlength_username():
    resp = requests.post(url=BASE_URL, json=fixtures.minlength_username)
    json_resp = resp.json()

    assert resp.status_code == 400
    assert 'min length is 4' in json_resp['meta']['description']['username']


def test_create_maxlength_username():
    resp = requests.post(url=BASE_URL, json=fixtures.maxlength_username)
    json_resp = resp.json()

    assert resp.status_code == 400
    assert 'max length is 20' in json_resp['meta']['description']['username']


# ----- Email -----
def test_create_witout_email():
    resp = requests.post(url=BASE_URL, json=fixtures.params_without_email)
    json_resp = resp.json()

    assert resp.status_code == 400
    assert 'email' in json_resp['meta']['description']

# TODO: check email field
