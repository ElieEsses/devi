import typer

app = typer.Typer()


@app.callback()
def main():
    """CLI template."""
    pass


@app.command()
def hello(name: str):
    typer.echo(f"Hello, {name}!")


@app.command()
def add(a: int, b: int, verbose: bool = False):
    result = a + b
    if verbose:
        typer.echo(f"Adding {a} and {b}")
    typer.echo(result)
