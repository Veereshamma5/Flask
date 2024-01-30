from http import HTTPStatus

import pytest
from config import TestConfig
from app import create_app


# Creating a client
@pytest.fixture
def client():
    test_app = create_app(TestConfig)
    with test_app.test_client() as test_client:
        yield test_client


def test_not_allowed_rest_call(client):
    res = client.get(
        '/learning/create'
    )
    assert res.status_code == HTTPStatus.METHOD_NOT_ALLOWED


# Positive scenario
def test_create_learning(client):
    req_json = {
        "associate_id": "8e733ba5-6ffc-4aea-ac65-3ff67a7ae771",
        "email": "veereshamma.k20@gmail.com",
        "skill_name": "Selenium",
        "learning_resource": "Python",
        "resource_link": "reqres.in",
        "duration": 10.9,
        "start_datetime": "2023-10-25 16:17:48",
        "end_datetime": "2029-10-25 16:17:48",
        "status": "In Progress"
    }
    res = client.post('/learning/create', json=req_json)
    assert res.status_code==HTTPStatus.CREATED

