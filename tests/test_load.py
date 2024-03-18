import uuid

import pytest

from dundie.core import load

from .constants import PEOPLE_FILE


@pytest.fixture(scope="function", autouse=True)
def create_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("new file content")
    yield
    file_.remove()


@pytest.mark.unit
@pytest.mark.high
def test_load():
    """Test load function."""
    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("arquivo indesejado")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == "J"
