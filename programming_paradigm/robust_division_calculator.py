def safe_divide(numerator, denominator):
    try:
        numerator_float = float(numerator)
        denominator_float = float(denominator)

        result = numerator_float / denominator_float
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")