from argparse import ArgumentParser

from .constants import NugitAbout

parser = ArgumentParser(
    prog=f"{NugitAbout.NAME}",
    description=NugitAbout.DESCRIPTION,
    add_help=True
)

parser.add_argument(
    "action",
    choices=("mount", "validate", "run", "remove"),
    help="specific action to perform",
)
