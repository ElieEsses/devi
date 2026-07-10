# devi

A growing personal dev tools CLI for scaffolding repos and managing project configs.

## Installation

### Prerequisites
- [`uv`](https://docs.astral.sh/uv/) — Python package/tool manager
- `make` (optional, only needed for `make install`)
- 
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
### General Usage
Once installed, use:

```devi <command> <arguments>```

Call ```devi --help``` for more details

### New Repo from Template
To create a new GitHub repository and clone locally use:
```
devi add <template> <project-name>
```
with either ```api```, ```cli```, or ```react``` as template.

### Add and sync .env files
To add an enviromental variable use:
```
devi env add <variable-name>
```
You will then be prompted to enter details.

Variable name will be added automatically to ```.env.example```. To supress use flag ```--no-ex```.
