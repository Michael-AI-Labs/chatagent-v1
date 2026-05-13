from agents import function_tool


@function_tool
def calculator(expression: str) -> str:
    """
    Evaluate a basic math expression.
    Example: '2 + 2 * 5'
    """

    try:
        result = eval(expression)
        return str(result)

    except Exception as error:
        return f"Calculation error: {error}"