from windsor_cli.src.client_helpers.decorators import raise_for_status_code


@raise_for_status_code
def validate_status_code(status_code: int) -> bool:
    return status_code == 200
