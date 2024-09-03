import os
from dataclasses import dataclass


@dataclass(init=False, frozen=True)
class About:
    NAME: str = "nugit"
    DESCRIPTION: str = ("A git-hooks tool that "
                        "works according to the script described"
                        " in the yaml configuration file.")
    VERSION: str = "1.1.0"
    AUTHOR: str = "Lev Zlobin (lengthylyova)"
    AUTHOR_EMAIL: str = "lengthylyova@gmail.com"


@dataclass(init=False, frozen=True)
class Paths:
    TEMPLATES_DIR: str = os.path.join(os.path.dirname(__file__), "templates")
    TEMPLATE_CFG_FILEPATH: str = os.path.join(TEMPLATES_DIR, "nugit.yaml")
    SCRIPT_TEMPLATE_FILEPATH: str = os.path.join(TEMPLATES_DIR, "base")

    CFG_DEST: str = os.path.join(os.path.curdir, "nugit.yaml")
    HOOKS_DEST: str = os.path.join(os.path.curdir, ".git/hooks/")


@dataclass(init=False, frozen=True)
class Color:
    BLUE: str = '\033[1;34m'
    GREEN: str = '\033[1;32m'
    RED: str = '\033[1;31m'
    CYAN: str = '\033[1;36m'
    PURPLE: str = '\033[1;35m'
    NO_COLOR: str = '\033[0m'


@dataclass(init=False, frozen=True)
class InOut:
    OUTPUT_HEADER: str = (f"\n{Color.PURPLE}{f'- nuGit v{About.VERSION} -'.center(28)}\n"
                          f"{'- Git - Hooks Tool -'.center(28)}\n\n")
    OUTPUT_FOOTER: str = f"\n{Color.GREEN}{'- nuGit jobs done -'.center(28)}{Color.NO_COLOR}\n\n"
