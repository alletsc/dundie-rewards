from unittest.mock import patch

import pytest

MARKER = """\
integration: Mark integration tests
unit: Mark unit tests
high: Mark high priority tests
medium: Mark medium priority tests
low: Mark low priority tests
"""


def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield


@pytest.fixture(autouse=True, escope="function")
def setup_test_database(request):
    """For each test, create an database file on tmpdir
    force database.py to user filepath"""
    tmpdir = request.getfixturevalue("tmpdir")
    test_db = str(tmpdir.join("database.json"))
    with patch("dundie.database.DATABASE_PATH", test_db):
        yield test_db
