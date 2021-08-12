from contextlib import contextmanager

from flask.testing import FlaskClient

from schafkopf_analyser import create_app


@contextmanager
def flask_test_client() -> FlaskClient:
    """
    Create a test client for simple use in tests

    Args:
        dependency_config: Config for dependency injection

    Returns:
        test client for the flask application
    """

    app = create_app(
        {"TESTING": True},
    )

    with app.test_client() as client:
        yield client
