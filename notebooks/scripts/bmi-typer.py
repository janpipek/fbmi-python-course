import typer


def bmi(weight: int, height: int):
    """Calculate BMI (Body Mass Index)."""
    result = weight / (height / 100) ** 2
    typer.echo(result)


if __name__ == "__main__":
    typer.run(bmi)