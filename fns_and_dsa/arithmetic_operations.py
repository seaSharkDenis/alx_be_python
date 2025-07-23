def perform_operation(num1, num2, operation):
    result = 0
    match operation:
        case "add":
            result = num1 + num2
        case "minus":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                result = "Cannot divide by zero."
            else:
                result = num1 / num2
    return result
