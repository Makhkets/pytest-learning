import pytest

@pytest.fixture
def clean_file_data():
    with open("tests/test_database.txt", "w"):
        pass


@pytest.fixture
def clean_file_data_end():
    with open("tests/test_database.txt", "w"):
        pass