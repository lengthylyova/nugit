from argparse import ArgumentParser

from .constants import About, Paths

parser = ArgumentParser(
    prog=f"{About.NAME}",
    description=About.DESCRIPTION,
    add_help=True
)

parser.add_argument(
    "action",
    choices=("mount", "run", "remove"),
    help="specific action to perform",
)

parser.add_argument(
    "-f", default=Paths.CFG_DEST, action="store",
)

parser.add_argument(
    "-s",
    action="append",
    choices=(
        "pre-commit", "pre-push",
        "pre-pull", "pre-rebase",
        "pre-receive", "pre-merge-commit",
        "pre-applypatch"
    ),
    required=True
)
