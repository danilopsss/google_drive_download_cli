from argparse import Namespace


def argument_resolver_helper(func):
    """
    This decorator aims to resolve the fields parsed by the user.

    It will evaluate - as an extra guarantee - if the user informed
    the parameters and formatting them - remove extra spaces, etc
    and raise an error If no value is present.
    """

    def wrapper(userargs: Namespace) -> list:
        namespace = func(userargs)()
        fields = [field.strip() for field in namespace.fields.split(",")]
        if not fields:
            raise ValueError
        return fields

    return wrapper


def argument_confirmation(func):
    """
    This decorator aims to validate with user the options.
    It will prompt a message and act accordingly.
    """

    def wrapper(args_to_confirm: Namespace):
        args = func(args_to_confirm)
        userconfirmation = input(
            "Your request is for the fields: "
            f"{', '.join(args[:-1])} and {args[-1]}.\n"
            "Do you confirm this request? [y/n]\n"
        )
        if userconfirmation[0] not in ["Y", "y"]:
            raise UserWarning
        return args

    return wrapper
