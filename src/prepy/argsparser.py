from argparse import ArgumentParser

from .constants import PrePyAbout

parser = ArgumentParser(
    prog=f"{PrePyAbout.NAME}",
    description=PrePyAbout.DESCRIPTION,
    add_help=True
)

parser.add_argument(
    "action",
    choices=("mount", "validate", "check"),
    help="specific action to perform",
)
