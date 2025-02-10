from pyguru.credentials.credentials_file import CredentialsFile
from tests.credentials.test_credentials import (TestCredentials,
                                                mock_credentials_file)


class TestCredentialsFile:

    def test_load(self, mock_credentials_file):
        username, password = CredentialsFile.load()
        assert username == TestCredentials.TEST_UNAME
        assert password == TestCredentials.TEST_PWD
