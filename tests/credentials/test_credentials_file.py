import configparser

import pytest

from pyguru.credentials.credentials_file import CredentialsFile
from tests.credentials.test_credentials import TEST_PWD, TEST_UNAME


@pytest.fixture
def mock_credentials_file(tmp_path, monkeypatch):
    credentials_path = tmp_path / 'credentials'

    config = configparser.ConfigParser()
    config['default'] = {
        CredentialsFile.UNAME_KEY: TEST_UNAME,
        CredentialsFile.PWD_KEY: TEST_PWD
    }

    with credentials_path.open('w') as f:
        config.write(f)

    monkeypatch.setattr(CredentialsFile, 'CREDENTIALS_FILEPATH', credentials_path)


def test_load(mock_credentials_file):
    username, password = CredentialsFile.load()
    assert username == TEST_UNAME
    assert password == TEST_PWD
