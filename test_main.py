from .main import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_list_fighters(client):
    rv = client.get("/api/v1/fighters")
    assert (
        b'[{"id":1,"name":"Daniel Cormier","weightclass":"Heavyweight (Up to 265 pounds)"},{"id":2,"name":"Jon Jones","weightclass":"Light heavyweight (205 lbs)"},{"id":3,"name":"Robert Whittaker","weightclass":"Middleweight (185 lbs)"},{"id":4,"name":"Kamaru Usman","weightclass":"Welterweight (170 lbs)"},{"id":5,"name":"Khabib Nurmagomedov","weightclass":"Lightweight (155 lbs)"},{"id":6,"name":"Max Holloway","weightclass":"Men\'s featherweight (145 lbs)"},{"id":7,"name":"Henry Cejudo","weightclass":"Men\'s bantamweight (135 lbs)"},{"id":8,"name":"Henry Cejudo","weightclass":"Men\'s flyweight (125 lbs)"},{"id":9,"name":"Amanda Nunes","weightclass":"Women\'s featherweight (145 lbs)"},{"id":10,"name":"Amanda Nunes","weightclass":"Women\'s Bantamweight (135 lbs)"},{"id":11,"name":"Valentina Shevchenko","weightclass":"Women\'s flyweight (125 lbs)"},{"id":12,"name":"Jessica Andrade","weightclass":"Strawweight (115 lbs)"}]\n'
        == rv.data
    )


def test_show_fighter_success(client):
    rv = client.get("/api/v1/fighters/2")
    assert (
        b'{"fighter":{"id":2,"name":"Jon Jones","weightclass":"Light heavyweight (205 lbs)"}}\n'
        == rv.data
    )

def test_show_fighter_failure_not_found(client):
    rv = client.get("/api/v1/fighters/40")
    assert 404 == rv.status_code


def test_create_fighter_success(client):
    rv = client.post("/api/v1/fighters", json={"name": "test", "weightclass": "test"})
    assert b'{"fighter":{"id":13,"name":"test","weightclass":"test"}}\n' == rv.data


def test_create_fighter_failure(client):
    rv = client.post("/api/v1/fighters", json={"name": "failure"})
    assert b'{"error":"400 - Bad Request"}\n' == rv.data


def test_update_fighter_success(client):
    rv = client.put(
        "/api/v1/fighters/1", json={"id": 1, "name": "test", "weightclass": "test"}
    )
    assert b'{"fighter":{"id":1,"name":"test","weightclass":"test"}}\n' == rv.data


def test_update_fighter_failure(client):
    rv = client.put("/api/v1/fighters/1", json={"name": "failure"})
    assert b'{"error":"400 - Bad Request"}\n' == rv.data

def test_destroy_fighter_success(client):
    rv = client.delete("/api/v1/fighters/4")
    assert b'{"fighter":{"id":4,"name":"Kamaru Usman","weightclass":"Welterweight (170 lbs)"}}\n' == rv.data

def test_destroy_fighter_failure_not_found(client):
    rv = client.delete("/api/v1/fighters/40")
    assert 404 == rv.status_code
