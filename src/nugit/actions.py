import os.path
import shutil
import stat
import subprocess

from .constants import Paths


def mount():
    if not os.path.exists(Paths.CFG_DEST):
        shutil.copy2(Paths.DEFAULT_CFG_FILEPATH, os.path.curdir)

    shutil.copy2(Paths.DEFAULT_PRECOMMIT_FILEPATH, Paths.PRECOMMIT_DEST)

    st = os.stat(Paths.PRECOMMIT_DEST)
    os.chmod(Paths.PRECOMMIT_DEST, st.st_mode | stat.S_IEXEC)


def run():
    if os.path.exists(Paths.PRECOMMIT_DEST):
        p = subprocess.Popen([Paths.PRECOMMIT_DEST])
        p.communicate()


def remove():
    if os.path.exists(Paths.PRECOMMIT_DEST):
        os.remove(Paths.PRECOMMIT_DEST)
