from datetime import datetime

from agents import function_tool


@function_tool
def calculator(expression: str) -> str:
    """
    Evaluate a basic math expression.
    """

    try:
        result = eval(expression)
        return str(result)

    except Exception as error:
        return f"Calculation error: {error}"


@function_tool
def current_time() -> str:
    """
    Return the current local date and time.
    """

    now = datetime.now()

    return now.strftime("%Y-%m-%d %H:%M:%S")


@function_tool
def unit_converter(value: float, from_unit: str, to_unit: str) -> str:
    """
    Convert between basic units.
    Supported:
    - miles ↔ kilometers
    - pounds ↔ kilograms
    """

    conversions = {
        ("miles", "kilometers"): value * 1.60934,
        ("kilometers", "miles"): value / 1.60934,
        ("pounds", "kilograms"): value * 0.453592,
        ("kilograms", "pounds"): value / 0.453592,
    }

    key = (from_unit.lower(), to_unit.lower())

    if key not in conversions:
        return "Unsupported conversion."

    result = conversions[key]

    return f"{value} {from_unit} = {result:.2f} {to_unit}"