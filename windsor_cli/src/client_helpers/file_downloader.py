import requests

from windsor_cli.src.client_helpers.third_party_configs import GoogleDrive
from windsor_cli.src.utils.conversions import convert_from_csv_to_dict
from windsor_cli.src.client_helpers.validations import validate_status_code


def get_request() -> requests.Response:
    file_id = GoogleDrive.TEST_TASK_DATA_FILE.value
    url = GoogleDrive.GOOGLE_DRIVE_DOWNLOAD_URL.value.format(file_id)
    params = GoogleDrive.GOOGLE_DRIVE_DOWNLOAD_PARAMS.value
    return requests.get(url=url, params=params)


def get_file_as_dictionary(*, fields: list):
    response = get_request()
    validate_status_code(response.status_code)
    decoded_content = response.content.decode("utf-8")

    return convert_from_csv_to_dict(
        csv_content=decoded_content.splitlines(), fields=fields
    )
