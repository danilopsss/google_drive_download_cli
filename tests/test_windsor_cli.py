import pytest

from windsor_cli.src.client_helpers.file_downloader import (
    get_file_as_dictionary,
)
from windsor_cli.src.client_helpers.exceptions import (
    GoogleDriveDownloadException,
)
from windsor_cli.src.utils.conversions import convert_from_csv_to_dict
from tests.mocked_data.classes import RequestsOK, RequestsNotFound


@pytest.fixture
def mocked_gdrive_data_ok(mocker):
    mocker.patch("requests.get", return_value=RequestsOK())


@pytest.fixture
def mocked_gdrive_data_not_found(mocker):
    mocker.patch("requests.get", return_value=RequestsNotFound())


def test_file_downloader(mocked_gdrive_data_ok):
    response = get_file_as_dictionary(fields=["column_1", "column_2"])
    expected = {"data": [{"column_1": "someData1", "column_2": "someData2"}]}
    assert response == expected


def test_file_downloader_with_only_one_field(mocked_gdrive_data_ok):
    response = get_file_as_dictionary(fields=["column_2"])
    expected = {"data": [{"column_2": "someData2"}]}
    assert response == expected


def test_file_downloader_with_404_status_code(mocked_gdrive_data_not_found):
    expected = "Error while retrieving the file [400]"
    with pytest.raises(GoogleDriveDownloadException) as exc_info:
        get_file_as_dictionary(fields=["column_1", "column_2"])
    assert exc_info.value.args[0] == expected


def test_convert_to_dict(mocked_gdrive_data_ok):
    request = RequestsOK()
    conversion_result = convert_from_csv_to_dict(
        csv_content=request.content.decode("utf-8").splitlines(),
        fields=["column_1"],
    )
    expected = {"data": [{"column_1": "someData1"}]}
    assert conversion_result == expected
