import pytest

from dundie.utils.email import check_valid_email
from dundie.utils.users import generate_simple_password


@pytest.mark.unit
@pytest.mark.parametrize(
    "adress", ["stella@costa.com", "joe@doe.com", "a@b.pt"]
)
def test_positive_check_valid_email(adress):
    """Ensure email is valid."""
    assert check_valid_email(adress) is True


@pytest.mark.unit
@pytest.mark.parametrize("adress", ["costa@.com", "@joedoe.com", "a@b"])
def test_negative_check_valid_email(adress):
    """Ensure email is valid."""
    assert check_valid_email(adress) is False


@pytest.mark.unit
def test_generate_simple_password():
    """Test generation of simple password.
    TODO: Generate a complex password, encrypit it."""
    passwords = []
    for i in range(100):
        passwords.append(generate_simple_password(8))

    assert len(set(passwords)) == 100
