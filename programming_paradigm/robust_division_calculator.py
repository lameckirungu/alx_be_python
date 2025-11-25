def safe_divide(numerator, denominator):
    """
    Performs division robustly, handling ValueError (non-numeric inputs)
    and ZeroDivisionError

    Args:
        numerator (float): The string representing the numerator.
        denominator (float): The string representing the denominator.

    Returns:
        float: The result of the division or an appropriate error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)

        try:
            res = num / den
            return f"The result of the division is {res}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
