import subprocess
import sys
from time import sleep
from typing import Dict, Any

import yaml

from .constants import Color, InOut
from .exeptions import NugitJobError, NugitError


def parse_yaml(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r") as file:
        data = yaml.safe_load(file)
    return data


def execute_cmd(cmd: str, quite: bool):
    p = subprocess.Popen(
        cmd, shell=True,
        stdout=subprocess.PIPE, universal_newlines=True
    )
    if not quite:
        for line in iter(p.stdout.readline, ""):
            yield line
        p.stdout.close()
    return_code = p.wait()
    if return_code:
        if quite:
            for line in iter(p.stdout.readline, ""):
                yield line
            p.stdout.close()
        raise NugitJobError(f"Failed: {cmd}")


def run_job(job_name: str, job_attrs: Dict[str, Any]) -> None:
    quite = job_attrs.get("quite", False)
    required = job_attrs.get("required", False)
    to_run = job_attrs.get("run", [])
    if not isinstance(required, bool):
        raise NugitError(f"`required` for {job_name} is not bool.")
    if not to_run:
        raise NugitError(f"`run` for {job_name} not defined.")

    sys.stderr.write(f"{Color.RED if required else Color.BLUE}"
                     f"({'req' if required else 'opt'}) {Color.NO_COLOR}"
                     f"{'(quite) ' if quite else ''}"
                     f"[{Color.BLUE}{job_name}{Color.NO_COLOR}]\n")

    for cmd in to_run:
        if not cmd:
            raise NugitJobError(f"empty command on {job_name}.")
        try:
            for line in execute_cmd(cmd, quite):
                sys.stdout.write(f"\t{Color.CYAN}>>> {Color.NO_COLOR}{line}")
        except NugitError as e:
            if not required:
                sys.stdout.write(f"{Color.RED}{e.__repr__()}{Color.NO_COLOR}")
            else:
                raise e


class JobsExecutor:
    def __init__(self, config_filepath: str, script_name: str) -> None:
        self.config_filepath = config_filepath
        self.script_name = script_name
        self.jobs = {}
        self.settings = {}

    def parse_config(self):
        data = parse_yaml(self.config_filepath)
        self.settings = data.get("settings", {})
        self.jobs = data.get("jobs", {})

    def run_jobs(self) -> None:
        sys.stdout.write(InOut.OUTPUT_HEADER)
        timeout = self.settings.get("timeout", 0)
        if not isinstance(timeout, (int, float)):
            raise NugitError("wrong settings.timeout type.")

        for job_name, job_attrs in self.jobs.items():
            if self.script_name not in job_attrs.get("with", []):
                continue
            run_job(job_name, job_attrs)
            sleep(timeout)
        sys.stdout.write(InOut.OUTPUT_FOOTER)

    def __enter__(self):
        self.parse_config()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type in (NugitJobError, NugitError):
            sys.exit(f"{Color.RED}{exc_type.__name__}: {exc_value}{Color.NO_COLOR}\n")
