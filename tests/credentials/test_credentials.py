
import configparser

import pytest

from pyguru.credentials.credentials import Credentials

TEST_UNAME = 'test_username'
TEST_PWD = 'test_password'


def test_env_credentials(monkeypatch):
    monkeypatch.setenv(Credentials.ENV_VAR_UNAME, TEST_UNAME)
    monkeypatch.setenv(Credentials.ENV_VAR_PWD, TEST_PWD)
    # Next fallthrough should be environment variables
    credentials = Credentials(username=None, password=None)
    assert TEST_UNAME == credentials.username
    assert TEST_PWD == credentials.password
