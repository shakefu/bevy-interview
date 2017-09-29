
# 3rd party libraries
from nose import SkipTest

# Package libraries
from .. import main


def test_permute_returns_list():
    result = main.permute("test")
    if not isinstance(result, list):
        raise Exception("Expect result to be list, got: " + type(result))


def test_permute_works_with_one_character():
    result = main.permute('a')

    if result != ['a']:
        raise Exception("Expected result of ['a'] got: " + str(result))


def test_permute_works_with_two_characters():
    result = main.permute('ab')
    result = set(result)

    if result != set(['ab', 'ba']):
        raise Exception("Expected result of set(['ab', 'ba']) got: "
                + str(result))


def test_permute_works_with_three_characters():
    result = main.permute('abc')
    result = set(result)

    expected = set(['abc', 'bac', 'cba', 'cab', 'acb', 'bca'])

    if result != expected:
        raise Exception("Expected result of " + str(expected) + " got: "
                + str(result))


def test_permute_works_with_simple_duplicates():
    result = main.permute('aaa')
    result = set(result)

    expected = set(['aaa'])

    if result != expected:
        raise Exception("Expected result of " + str(expected) + " got: "
                + str(result))


def test_permute_works_with_more_complex_duplicates():
    result = main.permute('aab')
    result = set(result)

    expected = set(['aab', 'baa', 'aba'])

    if result != expected:
        raise Exception("Expected result of " + str(expected) + " got: "
                + str(result))
