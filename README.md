<img src="assets/images/nugit_top.png">

## About
Easy to setup, simple to use and tasty as nugget pre-commit solution.

<img src="assets/images/nugit_terminal.png">

## Installation
```shell
pip install nugit
```

## Usage
### Mount
```shell
nugit mount
```
* creates an example `nugit.yaml` configuration file if not exists
* replaces the `pre-commit` file in your `.git/hooks/`

### Remove
```shell
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
    required: True # is successful completion required?
    run: # commands list
      - echo "Hi from Nugit!" # actual command
```
