import os.path
import shutil
import stat
import subprocess

from .constants import NugitPaths


def mount():
    if not os.path.exists(NugitPaths.CFG_DEST):
        shutil.copy2(NugitPaths.DEFAULT_CFG_FILEPATH, os.path.curdir)

    shutil.copy2(NugitPaths.DEFAULT_PRECOMMIT_FILEPATH, NugitPaths.PRECOMMIT_DEST)

    st = os.stat(NugitPaths.PRECOMMIT_DEST)
    os.chmod(NugitPaths.PRECOMMIT_DEST, st.st_mode | stat.S_IEXEC)


def run():
    if os.path.exists(NugitPaths.PRECOMMIT_DEST):
        p = subprocess.Popen([NugitPaths.PRECOMMIT_DEST])
        p.communicate()


def remove():
    if os.path.exists(NugitPaths.CFG_DEST):
        os.remove(NugitPaths.CFG_DEST)

    if os.path.exists(NugitPaths.PRECOMMIT_DEST):
        os.remove(NugitPaths.PRECOMMIT_DEST)
