from urllib import response
from flask import Flask
import json

from midterm_app import app

def test_midterm_app():
    response = app.test_client().get('/')
    assert response.status_code == 200