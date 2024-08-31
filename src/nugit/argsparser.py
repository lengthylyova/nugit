from argparse import ArgumentParser

from .constants import About

parser = ArgumentParser(
    prog=f"{About.NAME}",
    description=About.DESCRIPTION,
    add_help=True
)

parser.add_argument(
    "action",
    choices=("mount", "validate", "run", "remove"),
    help="specific action to perform",
)
