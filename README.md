# `pre-py`

<img src="https://i.imgur.com/HrSdjnP.png">

## About
Simple, lightweight and quick to install pre-commit solution.
Requires python and PyYAML installed in the environment

## Usage
### prepare `pre-commit` script
```shell
# go to local repo
cd some/insane/local/repo

# copy pre-commit script
cp path/to/pre-py/pre-commit .git/hooks/pre-commit

# add PyYAML into requirements.txt (requirements-dev.txt)
pip install PyYAML
```

### create `pre-py.yaml`
##### simple _example_
```yaml
jobs:
  echo:
    run:
      - echo "hello world!"
```

##### more advanced [_example_](./pre-py.yaml)
```yaml
settings:
  timeout: 0.5 # timeout between jobs (seconds)

jobs:
  git-branch: # job_name
    run: # commands list
      - git branch # actual command
  flake8-lint:
    required: False # if not required, the pre-commit will continue to work regardless of the error
    run:
      - flake8 --version
      - flake8 ./test.py
  python-tests:
    required: True
    run:
      - python -m unittest ./test.py -q
```

### Try it out
```shell
# try it out
git commit -m "first pre-py"

# if facing something like that:
#     hint: The '.husky/pre-commit' hook was ignored because it's not set as executable.
#     hint: You can disable this warning with git config advice.ignoredHook false.
# use this:
chmod ug+x .git/hooks/*
```
