from enum import Enum
import typer
from typing import Annotated


class HeightUnit(str, Enum):
    cm = "cm"
    m = "m"
    in_ = "in"
    ft = "ft"

    def __str__(self) -> str:
        return self.value


class WeightUnit(str, Enum):
    kg = "kg"
    lb = "lb"

    def __str__(self) -> str:
        return self.value


def _convert_height(height, unit: HeightUnit):
    """Convert any height to m."""
    if unit == HeightUnit.m:
        return height
    if unit == HeightUnit.cm:
        return height / 100
    if unit == HeightUnit.in_:
        return height * 0.0254
    if unit == HeightUnit.ft:
        return height * 0.3048
    

def _convert_weight(weight, unit: WeightUnit):
    """Convert any weight to kg."""
    if unit == WeightUnit.kg:
        return weight
    if unit == WeightUnit.lb:
        return weight * 0.453592


def bmi(
    weight: Annotated[float, typer.Argument(help="Weight in the selected weight units")],
    height: Annotated[float, typer.Argument(help="Height in the selected height units")],
    height_unit: Annotated[HeightUnit, typer.Option(help="cm | m | in | ft")] = HeightUnit.cm,
    weight_unit: Annotated[WeightUnit, typer.Option(help="kg | lb")] = WeightUnit.kg

):
    """Calculate BMI (Body Mass Index)."""
    weight = _convert_weight(weight, weight_unit)
    height = _convert_height(height, height_unit)

    result = weight / height ** 2
    typer.echo(result)


if __name__ == "__main__":
    typer.run(bmi)