import os
from dataclasses import dataclass


@dataclass(init=False, frozen=True)
class NugitAbout:
    NAME: str = "nugit"
    DESCRIPTION: str = ("A pre-commit solution tool that "
                        "works according to the script described"
                        " in the `nugit.yaml` configuration file.")
    VERSION: str = "1.0.8"
    AUTHOR: str = "Lev Zlobin (lengthylyova)"
    AUTHOR_EMAIL: str = "lengthylyova@gmail.com"


@dataclass(init=False, frozen=True)
class NugitPaths:
    DEFAULT_CFG_FILEPATH: str = os.path.join(os.path.dirname(__file__), "defaults/nugit.yaml")
    DEFAULT_PRECOMMIT_FILEPATH: str = os.path.join(os.path.dirname(__file__), "defaults/pre-commit")

    CFG_DEST: str = os.path.join(os.path.curdir, "nugit.yaml")
    PRECOMMIT_DEST: str = os.path.join(os.path.curdir, ".git/hooks/pre-commit")
