
from utils import file_worker
from conftest import clean_file_data

def test_write_and_check(clean_file_data):
    string = "12345"
    file_worker.write_file("tests/test_database.txt", string)
    with open("tests/test_database.txt", "r+") as file:
        data = file.read()
    assert data == string


def test_write_and_check2(clean_file_data):
    string = "123457"
    file_worker.write_file("tests/test_database.txt", string)
    with open("tests/test_database.txt", "r+") as file:
        data = file.read()
    assert data == string

