import pytest

import app as main


@pytest.fixture
def app():
    instance = main.create_app()
    instance.debug = True
    return instance.test_client()


def test_hello_world(app):
    res = app.get("/")
    # print(dir(res), res.status_code)
    assert res.status_code == 200
    assert b"Hello World" in res.data

