import configparser
from pathlib import Path

import pytest

from pyguru.credentials.credentials_file import CredentialsFile
from tests.credentials.test_credentials import (TestCredentials,
                                                mock_credentials_file)


@pytest.fixture
def credentials_tmp_filepath(tmpdir):
    yield Path(tmpdir) / 'credentials'


class TestCredentialsFile:

    def test_load(self, mock_credentials_file):
        username, password = CredentialsFile.load()
        assert username == TestCredentials.TEST_UNAME
        assert password == TestCredentials.TEST_PWD

    def test_write_new_file(self, credentials_tmp_filepath):
        CredentialsFile.write(
            username=TestCredentials.TEST_UNAME,
            password=TestCredentials.TEST_PWD,
            filepath=credentials_tmp_filepath
        )
        config = configparser.ConfigParser()
        config.read(credentials_tmp_filepath)
        assert config.get(CredentialsFile.DEFAULT_PROFILE_NAME, CredentialsFile.UNAME_KEY) == TestCredentials.TEST_UNAME
        assert config.get(CredentialsFile.DEFAULT_PROFILE_NAME, CredentialsFile.PWD_KEY) == TestCredentials.TEST_PWD
