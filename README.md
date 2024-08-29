<img src="assets/images/lesa7xg.png">

## About `nugit`
Easy to setup, simple to use and tasty as nugget pre-commit solution.

<img src="assets/images/k9x8fAf.png">

## Installation
```console
pip install nugit
```

## Usage
### Mount
```console
nugit mount
```
* creates an example `nugit.yaml` configuration file if not exists
* replaces the `pre-commit` file in your `.git/hooks/`

### Run (check)
```console
nugit run
```
* runs `.git/hooks/pre-commit` script if exists

### Remove
```console
nugit remove
```
* removes a `nugit.yaml` configuration file
* removes the `pre-commit` file in your `.git/hooks/`

### `nugit.yaml` example
```yaml
settings:
  timeout: 0.5 # timeout between jobs (seconds)

jobs:
  greeting: # job_name
    quite: False # nugit ignores job output if True (default=False)
    required: True # is successful completion required?
    run: # commands list
      - echo "Hi from Nugit!" # actual command
```
