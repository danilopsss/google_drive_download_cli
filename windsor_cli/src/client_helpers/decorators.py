from src.client_helpers.exceptions import (
    GoogleDriveDownloadException,
)


def raise_for_status_code(func):
    def wrapper(status_code: int):
        if not func(status_code):
            raise GoogleDriveDownloadException(
                f"Error while retrieving the file [{status_code}]"
            )

    return wrapper
