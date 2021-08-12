import pytest

from sisosign import __version__
from sisosign.sisosign import sisosign


def test_version():
    assert __version__ == "0.1.0"


def test_returns_with_a_list_of_one_person():
    people = ["Bill"]
    expected = "Bill"
    assert expected == sisosign(people)


def test_returns_one_person_with_a_list_of_two_people():
    people = ["Dipper", "Mabel"]
    actual = sisosign(people)
    assert type(actual) == str


def test_returns_one_person_with_a_list_of_three_people():
    people = ["Uncle Stan", "Soos", "Wendy"]
    actual = sisosign(people)
    assert type(actual) == str


def test_throws_exception_for_an_empty_list():
    with pytest.raises(Exception):
        sisosign([])
