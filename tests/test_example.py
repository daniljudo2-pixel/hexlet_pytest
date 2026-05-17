from hexlet_pytest.example import reverse
from pathlib import Path


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

def read_file(filename):
    return get_test_data_path(filename).read_text()

def test_reverse():
    before_text = read_file('text_before.txt')
    after_text = read_file('text_after')
    actual = reverse(before_text)

    assert actual == after_text