import os.path
import shutil
import stat
import subprocess
from argparse import Namespace

from jinja2 import Environment, select_autoescape, FileSystemLoader

from .constants import Paths
from .exeptions import NugitError


def render_template(name: str, environment: dict) -> str:
    return Environment(
        loader=FileSystemLoader(Paths.TEMPLATES_DIR),
        autoescape=select_autoescape()
    ).get_template(name).render(**environment)


def mount(args: Namespace):
    if not os.path.exists(args.f):
        with open(args.f, "w") as file:
            file.write(render_template(name="cfg.yaml", environment={"scripts": args.s}))

    for script_name in args.s:
        script_dest = os.path.join(Paths.HOOKS_DEST, script_name)
        with open(script_dest, "w") as file:
            file.write(render_template(
                name="base",
                environment={
                    "script_name": script_name,
                    "config_filepath": args.f
                }
            ))
        st = os.stat(script_dest)
        os.chmod(script_dest, st.st_mode | stat.S_IEXEC)


def run(args):
    scripts = args.s
    if len(scripts) > 1:
        raise NugitError("Only one script may be selected to run.")

    filepath = os.path.join(Paths.HOOKS_DEST, scripts[0])
    if os.path.exists(filepath):
        p = subprocess.Popen([filepath])
        p.communicate()


def remove(args):
    for script_name in args.s:
        script_dest = os.path.join(Paths.HOOKS_DEST, script_name)
        if os.path.exists(script_dest):
            os.remove(script_dest)
