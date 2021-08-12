# Given
from pathlib import Path

from assertpy import assert_that


def test_init():
    # Given
    path_to_init = Path('../schafkopf_analyser/__init__.py')

    # When
    with open(path_to_init, 'r') as f:
        file_content = f.readlines()

    # Then
    assert_that(file_content[0]).contains("from .flask_factory import create_app")


def test_main():
    # Given
    path_to_main = Path('../schafkopf_analyser/__main__.py')

    # When
    with open(path_to_main, 'r') as f:
        file_content = f.readlines()

    # Then
    assert_that(file_content[0]).contains("from waitress import serve")

    assert_that(file_content[2]).contains('from schafkopf_analyser import create_app')

    assert_that(file_content[4]).contains('serve(create_app(), host=\'127.0.0.1\', port="5000"')
