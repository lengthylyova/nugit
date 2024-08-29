import os.path
import shutil
import stat

from .constants import PrePyPaths


def mount():
    if not os.path.exists(PrePyPaths.CFG_DEST):
        shutil.copy2(PrePyPaths.DEFAULT_CFG_FILEPATH, os.path.curdir)

    shutil.copy2(PrePyPaths.DEFAULT_PRECOMMIT_FILEPATH, PrePyPaths.PRECOMMIT_DEST)

    st = os.stat(PrePyPaths.PRECOMMIT_DEST)
    os.chmod(PrePyPaths.PRECOMMIT_DEST, st.st_mode | stat.S_IEXEC)


def remove():
    if os.path.exists(PrePyPaths.CFG_DEST):
        os.remove(PrePyPaths.CFG_DEST)

    if os.path.exists(PrePyPaths.PRECOMMIT_DEST):
        os.remove(PrePyPaths.PRECOMMIT_DEST)
