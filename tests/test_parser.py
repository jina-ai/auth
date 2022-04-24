import pytest
from argparse import ArgumentParser
from auth.parsers import get_main_parser

@pytest.fixture
def parser() -> 'ArgumentParser':
    return get_main_parser()

@pytest.mark.parametrize('input,expected', [
    (['login'], 'login'),
    (['logout'], 'logout'),
])
def test_login_logout(parser: 'ArgumentParser', input, expected):
    assert parser.parse_args(input).cli == expected


@pytest.mark.parametrize('input,expected', [
    (['token', 'create', 'foo'], ['token', 'create', 7, 'foo']),
    (['token', 'create', '-e', '10', 'foo'], ['token', 'create', 10, 'foo']),
    (['token', 'create', '--expire', '10', 'foo'], ['token', 'create', 10, 'foo']),
])
def test_token_create(parser: 'ArgumentParser', input, expected):
    assert parser.parse_args(input).cli == expected[0]
    assert parser.parse_args(input).operation == expected[1]
    assert parser.parse_args(input).expire == expected[2]
    assert parser.parse_args(input).name == expected[3]

@pytest.mark.parametrize('input,expected', [
    (['token', 'delete', 'foo'], ['token', 'delete', 'foo']),
])
def test_token_delete(parser: 'ArgumentParser', input, expected):
    assert parser.parse_args(input).cli == expected[0]
    assert parser.parse_args(input).operation == expected[1]
    assert parser.parse_args(input).name == expected[2]