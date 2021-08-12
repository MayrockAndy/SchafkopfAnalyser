from http import HTTPStatus

from assertpy import assert_that

from .flask_utils import flask_test_client


def test_index(client: flask_test_client()):
    res = client.get('/', follow_redirects=True)
    assert_that(res.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(res.data).is_equal_to(b'test')
