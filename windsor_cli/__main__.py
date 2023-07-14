import json

from src.cli_helpers.cli import cli_arguments_extractor
from src.client_helpers.file_downloader import (
    get_file_as_dictionary,
)
from src.client_helpers.exceptions import (
    GoogleDriveDownloadException,
)


def entrypoint() -> dict:
    fields = cli_arguments_extractor()
    return get_file_as_dictionary(fields=fields)


if __name__ == "__main__":
    try:
        json_response = json.dumps(entrypoint(), indent=4)
        print(json_response)
    except GoogleDriveDownloadException as exc_info:
        print(exc_info.args[0])
    except UserWarning:
        print("!" * 5, "Operation cancelled.", "!" * 5)
