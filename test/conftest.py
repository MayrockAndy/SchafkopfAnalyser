import pytest

from .flask_utils import flask_test_client


@pytest.fixture
def client():
    """Create flask test client with no dependency injection override"""
    with flask_test_client() as client:
        yield client
