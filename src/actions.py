import os.path
import shutil
import stat

from src.constants import PrePyPaths


def mount():
    if not os.path.exists(PrePyPaths.CFG_DEST):
        shutil.copy2(PrePyPaths.DEFAULT_CFG_FILEPATH, os.path.curdir)

    if os.path.exists(PrePyPaths.PRECOMMIT_DEST):
        shutil.copy2(PrePyPaths.PRECOMMIT_DEST, PrePyPaths.PRECOMMIT_OLD_DEST)

    shutil.copy2(PrePyPaths.DEFAULT_PRECOMMIT_FILEPATH, PrePyPaths.PRECOMMIT_DEST)

    st = os.stat(PrePyPaths.PRECOMMIT_DEST)
    os.chmod(PrePyPaths.PRECOMMIT_DEST, st.st_mode | stat.S_IEXEC)
