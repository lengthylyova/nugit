<img src="assets/images/lesa7xg.png">

[![Flake8](https://github.com/lengthylyova/nugit/actions/workflows/flake8-lint.yaml/badge.svg)](https://github.com/lengthylyova/nugit/actions/workflows/flake8-lint.yaml)
![PyPI - Version](https://img.shields.io/pypi/v/nugit)
![GitHub License](https://img.shields.io/github/license/lengthylyova/nugit)
![PyPI - Downloads](https://img.shields.io/pypi/dm/nugit)

---

## About `nugit`

A git-hooks tool that works according to the script described in the yaml configuration file.

<img src="assets/images/k9x8fAf.png">

---

## Quick Guide

### Installation

```console
pip install nugit
```

---

### Integration

To integrate nugit into your project, you need to mount it.
To do this, **use the `mount`** command.
Declare the **git hooks you intend to use** using the `-s` flag.

```console
nugit mount -s pre-commit -s pre-push
```

This command will create git hooks in your local repository and
a `nugit.yaml` (if not exist) with [basic configuration](#basic-configuration) for the **selected** git hooks.
You can also specify your own path to the configuration file using the `-f` flag.

```console
nugit mount -s pre-commit -s pre-push -f "my-nugit-cfg.yaml"
```

**_Warning_**:
_This will **_create or replace an existing declared git hook_** in your
project's `.git/hooks/` directory._

---

### Test runs

You can run any git hook without calling git itself.
To do this, use the `run` command with selected to run script using the `-s` flag.

```console
nugit run -s pre-commit
```

---

### Remove hooks

If you no longer need a git hook, you can remove it without changing the configuration.
To do this, use the `remove` command. As with the other cases, select the scripts to remove using the `-s` flag.

```console
nugit remove -s pre-commit -s pre-push
```

---

### Configuration file
#### Basic configuration
```yaml
settings:
  timeout: 0.5 # timeout between jobs (seconds)

jobs:
  greeting: # job_name
    with: {{scripts}} # scripts list to use this job
    quite: False # nugit ignores job output if True (default=False) and no error occurred
    required: True # is successful completion required?
    run: # commands list
      - echo "Hi from Nugit!" # actual command
```

#### A more realistic use case
```yaml
settings:
  timeout: 0.5

jobs:
  vpn-check:
    with: ["pre-push"]
    required: True
    run:
      - |
        python << END
        import requests
        
        print("Requesting for my ip...")
        response = requests.get("https://api.ipify.org?format=json").json()
        if response.get("ip", None) != "${MY_VPN_IP}":
          sys.exit("VPN not enabled!")
        print("Everything ok!")
        END
        
  flake8-lint:
    with: ["pre-commit"]
    quite: True
    run:
      - flake8 --version
      - flake8 src/* --statistics --ignore F401 --max-line-length=100
  
  py-unittests:
    with: ["pre-commit", "pre-push"]
    quite: True
    required: True
    run:
      - python -m unittest
```

---

### Possible values for `-s` flag:

* `pre-commit`
* `pre-push`
* `pre-pull`
* `pre-rebase`
* `pre-recieve`
* `pre-merge-commit`
* `pre-apply-patch`




















