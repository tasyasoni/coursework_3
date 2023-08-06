from utils.class_functions import Operations
import pytest

@pytest.fixture
def operations_instans():
    instans = Operations("EXECUTED",
                         "2019-08-26",
                         "Перевод организации",
                         "9589",
                         "31957.58",
                         "руб.",
                         "Maestro 1596837868705199")
    return instans

def test_is_state_correct(operations_instans):
    assert operations_instans.is_state_correct() == True


def test_date_mirror(operations_instans):
    assert operations_instans.date_mirror() == ("26.08.2019")


def test_code_count_number(operations_instans):
    assert operations_instans.code_count_number() == ("Maestro 1596 83** **** 5199")


@pytest.fixture
def operations_instans1():
    instans1 = Operations("",
                         "2019-08-26",
                         "Перевод организации",
                         "9589",
                         "31957.58",
                         "руб.",
                         "Счет 75106830613657916952")
    return instans1

def test_is_state_correct1(operations_instans1):
    assert operations_instans1.is_state_correct() == False


def test_code_count_number1(operations_instans1):
    assert operations_instans1.code_count_number() == ("Счет 7510 68** **** **** 6952")




