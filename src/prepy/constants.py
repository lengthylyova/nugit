import os
from dataclasses import dataclass


@dataclass(init=False, frozen=True)
class PrePyAbout:
    NAME: str = "prepy"
    DESCRIPTION: str = "Easy to understand, configure and install git pre-commit solution"
    VERSION: str = "1.0.0"
    AUTHOR: str = "Lev Zlobin (lengthylyova)"
    AUTHOR_EMAIL: str = "lengthylyova@gmail.com"


@dataclass(init=False, frozen=True)
class PrePyPaths:
    DEFAULT_CFG_FILEPATH: str = os.path.join(os.path.dirname(__file__), "defaults/prepy.yaml")
    DEFAULT_PRECOMMIT_FILEPATH: str = os.path.join(os.path.dirname(__file__), "defaults/pre-commit")

    CFG_DEST: str = os.path.join(os.path.curdir, "prepy.yaml")
    PRECOMMIT_DEST: str = os.path.join(os.path.curdir, ".git/hooks/pre-commit")
    PRECOMMIT_OLD_DEST: str = os.path.join(os.path.curdir, ".git/hooks/pre-commit.old")
