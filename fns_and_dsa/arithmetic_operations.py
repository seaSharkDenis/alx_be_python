def perform_operation(num1, num2, operation):
    result = 0
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            result = "Cannot divide by zero."
        else:
            result = num1 / num2
    return result
