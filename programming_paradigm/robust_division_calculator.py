def safe_divide(numerator, denominator):
    try:
        numerator_float = float(numerator)
        denominator_float = float(denominator)

        result = numerator_float / denominator_float
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."