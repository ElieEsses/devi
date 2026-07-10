import re
import shutil
import subprocess
from enum import StrEnum
from pathlib import Path

import typer
from dotenv import dotenv_values, set_key
from rich import print

app = typer.Typer()
env_app = typer.Typer(help="Manage environment variables")

app.add_typer(env_app, name="env")


@app.callback()
def main():
    """CLI template."""
    pass


TEMPLATES = {
    "cli": "https://github.com/ElieEsses/python-cli-template",
    "api": "https://github.com/ElieEsses/python-api-template.git",
    "react": "https://github.com/ElieEsses/react-ui-template.git",
}


class Template(StrEnum):
    cli = "cli"
    api = "api"
    react = "react"


@app.command()
def new(
    template: Template,
    name: str,
    local: bool = typer.Option(
        False,
        "--local",
        "-l",
        help="Create the project locally without creating a GitHub repository.",
    ),
    public: bool = typer.Option(
        False,
        help="Create a public GitHub repository.",
    ),
):
    """Create a new project from one of your templates: api, cli, or react"""

    if Path(name).exists():
        print(f"[red]Directory already exists: {name}[/red]")
        raise typer.Exit(1)

    if local:
        subprocess.run(
            ["git", "clone", TEMPLATES[template], name],
            check=True,
        )

        shutil.rmtree(Path(name) / ".git")

        subprocess.run(
            ["git", "-C", name, "init"],
            check=True,
        )
    else:
        command = [
            "gh",
            "repo",
            "create",
            name,
            "--template",
            TEMPLATES[template],
            "--clone",
            "--private" if not public else "--public", 
        ]

        subprocess.run(command, check=True)

    print(f"[green]Created {name} from {TEMPLATES[template]}[/green]")
    print("")
    print("Next:")
    print(f"  cd {name}")

    if template in {"cli", "api"}:
        print("  uv sync")
    elif template == "react":
        print("  npm install")


ENV_KEY_PATTERN = re.compile(r"^[A-Z_][A-Z0-9_]*$")
SECRET_SUFFIXES = ("_KEY", "_SECRET", "_TOKEN", "_PASSWORD")


@env_app.command()
def add(keys: list[str], no_ex: bool = False):
    """Add one or more environment variables."""

    env_file = Path(".env")
    example_env_file = Path(".env.example")

    env_file.touch(exist_ok=True)
    example_env_file.touch(exist_ok=True)

    existing = dotenv_values(env_file)
    example_existing = dotenv_values(example_env_file)

    for key in keys:
        key = key.upper()

        if not ENV_KEY_PATTERN.fullmatch(key):
            print(f"[red]Invalid environment variable name: {key}[/red]")
            continue

        if key in existing:
            overwrite = typer.confirm(
                f"{key} already exists. Overwrite?",
                default=False,
            )
            if not overwrite:
                continue

        hidden = key.endswith(SECRET_SUFFIXES)

        value = typer.prompt(
            f"Enter value for {key}",
            hide_input=hidden,
        )

        set_key(str(env_file), key, value)
        existing[key] = value
        if not no_ex:
            if key not in example_existing:
                set_key(
                    str(example_env_file),
                    key,
                    "",
                    quote_mode="never",
                )
                example_existing[key] = ""
    if not no_ex:
        print(
            f"[green]Added [bold]{key}[/bold] to {env_file}"
            f" and placeholder to {example_env_file}[/green]"
        )
    if no_ex:
        print(f"[green]Added [bold]{key}[/bold] to {env_file}.")
