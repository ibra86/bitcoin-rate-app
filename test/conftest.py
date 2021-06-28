import pytest

from app import app as flask_app  # noqa


@pytest.fixture(scope="module")
def app():
    yield flask_app


@pytest.fixture(scope="module")
def client(app):
    app.config.update(TESTING=True)
    return app.test_client()
