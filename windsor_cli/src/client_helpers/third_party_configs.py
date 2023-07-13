from enum import Enum


class GoogleDrive(Enum):
    """
    This module is responsible for hold the configurations
    related to the download parameters of google drive.

    It could change any time.

    Attributes:
        TEST_TASK_DATA_FILE: The Id of the file on google drive.
        GOOGLE_DRIVE_DOWNLOAD_URL: The main endpoint.
        GOOGLE_DRIVE_DOWNLOAD_PARAMS = Standard params for download.
    """

    TEST_TASK_DATA_FILE = ""
    GOOGLE_DRIVE_DOWNLOAD_URL = "https://drive.google.com/uc?id={}"
    GOOGLE_DRIVE_DOWNLOAD_PARAMS = {"export": "download"}
