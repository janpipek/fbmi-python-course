import click

def bmi(weight, height):
    return weight / height ** 2

@click.command
@click.argument("weight", type=int)
@click.argument("height", type=int)
def run_bmi(weight, height):
    """Calculate BMI (Body Mass Index)."""
    print(bmi(weight, height / 100))

if __name__ == "__main__":
    run_bmi()