# devi

A growing personal dev tools CLI.

## Installation

**Prerequisites**
- [`uv`](https://docs.astral.sh/uv/) — Python package/tool manager
- `make`

**Quick install:**
```bash
make install
```

**Manual:**
```bash
uv sync
uv tool install -e .
```

Verify: `devi --help`

Uninstall: `uv tool uninstall devi`

## Usage
Once installed, use:

```devi <command> <arguments>```

Call ```devi --help``` for more details

**New repo from template**

To create a new GitHub repository and clone locally use:
```
devi add <template> <project-name>
```
with either ```api```, ```cli```, or ```react``` as template.

Use tag ```-local``` to only create repo locally, not in GitHub.

Use tag. ```-public``` to make repo public instead of private.

**Add and sync .env files**

To add an enviromental variable use:
```
devi env add <variable-name>
```
You will then be prompted to enter details.

Variable name will be added automatically to ```.env.example```. To supress use flag ```--no-ex```.
