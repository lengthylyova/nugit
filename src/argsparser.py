from argparse import ArgumentParser

from src.constants import PrePyAbout

parser = ArgumentParser(
    prog=f"{PrePyAbout.NAME}",
    description=PrePyAbout.DESCRIPTION,
    add_help=True
)

parser.add_argument(
    "action",
    choices=("mount", "validate"),
    help="specific action to perform",
)
