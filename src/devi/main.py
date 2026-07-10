from enum import StrEnum
import subprocess
from pathlib import Path

import typer

app = typer.Typer()


@app.callback()
def main():
    """CLI template."""
    pass


TEMPLATES = {
    "cli": "https://github.com/ElieEsses/python-cli-template",
    "api": "https://github.com/ElieEsses/python-api-template.git",
    "react": "elieesses04/react-ui-template",
}

class Template(StrEnum):
    cli = "cli"
    api = "api"
    react = "react"
    
@app.command()
def new(template: Template, name: str, 
        private: bool = typer.Option(
            True,
            help="Create a private GitHub repository.",
        )
    ):
    """Create a new project from one of your templates: api, cli, or react"""
    if template not in TEMPLATES:
        typer.secho(
            f"Unknown template: {template}",
            fg=typer.colors.RED,
        )
        typer.echo(f"Available templates: {', '.join(TEMPLATES)}")
        raise typer.Exit(1)

    if Path(name).exists():
        typer.secho(
            f"Directory already exists: {name}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    command = [
        "gh",
        "repo",
        "create",
        name,
        "--template",
        TEMPLATES[template],
        "--clone",
    ]

    command.append("--private" if private else "--public")

    subprocess.run(command, check=True)

    typer.secho(
        f"Created {name} from {TEMPLATES[template]}",
        fg=typer.colors.GREEN,
    )
    typer.echo("")
    typer.echo("Next:")
    typer.echo(f"  cd {name}")

    if template in {"cli", "api"}:
        typer.echo("  uv sync")
    elif template == "react":
        typer.echo("  npm install")
