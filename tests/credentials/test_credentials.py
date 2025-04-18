
import configparser

import pytest

from pyguru.credentials.credentials import Credentials
from pyguru.credentials.credentials_file import CredentialsFile


@pytest.fixture
def mock_credentials_file(tmp_path, monkeypatch):
    credentials_path = tmp_path / 'credentials'

    config = configparser.ConfigParser()
    config['default'] = {
        CredentialsFile.UNAME_KEY: TestCredentials.TEST_UNAME,
        CredentialsFile.PWD_KEY: TestCredentials.TEST_PWD
    }

    with credentials_path.open('w') as f:
        config.write(f)

    monkeypatch.setattr(CredentialsFile, 'CREDENTIALS_FILEPATH', credentials_path)


class TestCredentials:

    TEST_UNAME = 'test_username'
    TEST_PWD = 'test_password'
    ENV_VAR_UNAME = 'PYGURU_USERNAME'
    ENV_VAR_PWD = 'PYGURU_PASSWORD'

    def test_parameter_credentials(self):
        credentials = Credentials(username=TestCredentials.TEST_UNAME, password=TestCredentials.TEST_PWD)
        assert credentials.data.username == TestCredentials.TEST_UNAME
        assert credentials.data.password == TestCredentials.TEST_PWD

    def test_env_credentials(self, monkeypatch):
        monkeypatch.setenv(self.ENV_VAR_UNAME, TestCredentials.TEST_UNAME)
        monkeypatch.setenv(self.ENV_VAR_PWD, TestCredentials.TEST_PWD)
        # Next fallthrough should be environment variables
        credentials = Credentials(username=None, password=None)
        assert credentials.data.username == TestCredentials.TEST_UNAME
        assert credentials.data.password == TestCredentials.TEST_PWD

    def test_env_config_file(self, monkeypatch, mock_credentials_file):
        """
        Verify that when no credentials are supplied via arguments or environment variables, the config file is being used.
        """
        monkeypatch.setenv(self.ENV_VAR_UNAME, '')
        monkeypatch.setenv(self.ENV_VAR_PWD, '')
        credentials = Credentials(username=None, password=None)
        assert credentials.data.username == TestCredentials.TEST_UNAME
        assert credentials.data.password == TestCredentials.TEST_PWD
