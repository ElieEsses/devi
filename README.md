## Description
A growing personal dev tools CLI.

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

## Installation

To install project dependencies, and install the CLI globally in editable mode:
```bash
make install
```

or

Install the project dependencies:

```bash
uv sync
```

and install the CLI:

```bash
uv tool install -e .
```

Verify the installation:

```bash
cli-name --help
```

To uninstall:

```bash
uv tool uninstall cli-name
```
