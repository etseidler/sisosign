from click.testing import CliRunner

from sisosign.sisosign import sisosign


def test_works_with_a_list_of_one_person():
    people = ["Bill"]
    runner = CliRunner()
    result = runner.invoke(sisosign, people)
    assert result.exit_code == 0
    assert result.output == "Bill should stay\n"


def test_prints_one_person_with_a_list_of_two_people():
    people = ["Dipper", "Mabel"]
    runner = CliRunner()
    result = runner.invoke(sisosign, people)
    assert result.exit_code == 0
    assert len(result.output.split()) == 3
    assert result.output.split()[0] in people


def test_prints_one_person_with_a_list_of_three_people():
    people = ["Uncle Stan", "Soos", "Wendy"]
    runner = CliRunner()
    result = runner.invoke(sisosign, people)
    assert result.exit_code == 0
    assert " ".join(result.output.split()[:-2]) in people


def test_throws_exception_for_an_empty_list():
    people = []
    runner = CliRunner()
    result = runner.invoke(sisosign, people)
    assert result.exit_code == 1
    assert (
        result.output
        == "Please provide at least one name or use the --help option.\n"
    )
