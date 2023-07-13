from csv import DictReader


def convert_from_csv_to_dict(*, csv_content: list, fields: list) -> dict:
    """
    The method responsible to convert the incoming list - each list
    is a row of the csv file - to standardized output object.

    Here it will be considered only the fields specified in the
    parameters.

    Arguments:
        csv_content (list): Parsed rows of CSV
        fields (list): fields to be used in the filtering. All
        non present fields will be discarded.
    """
    handled_data = []
    for row in DictReader(csv_content, delimiter=","):
        handled_data.append(
            dict(filter(lambda line: line[0] in fields, row.items()))
        )
    return {"data": handled_data}
