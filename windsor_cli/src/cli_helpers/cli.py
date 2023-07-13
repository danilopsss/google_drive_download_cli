from argparse import Namespace, ArgumentParser
from windsor_cli.src.cli_helpers.decorators import (
    argument_resolver_helper,
    argument_confirmation,
)


@argument_confirmation
@argument_resolver_helper
def argument_resolver(args: Namespace) -> Namespace:
    return args


def cli_arguments_extractor():
    arguments = ArgumentParser(prog="A simple file retriever from GDrive")
    arguments.add_argument("--fields", default=None, required=True)

    return argument_resolver(arguments.parse_args)
