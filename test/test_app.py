from app import app
from flask import json


def test_home_route():
    respone = app.test_client().get("/")
    assert respone.status_code == 200
    assert type(respone.data) == bytes


def test_hi_route():
    respone = app.test_client().get("/hi/bharath")
    assert respone.status_code == 200


def test_bye_route():
    respone = app.test_client().get("/bye")
    assert respone.status_code == 200
