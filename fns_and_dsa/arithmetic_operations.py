

def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            answer = num1 + num2
        case 'subtract':
            answer = num1 - num2
        case 'multiply':
            answer = num1 * num2
        case 'divide':
            if num2 != 0:
                answer = num1 / num2
            elif num2 == 0:
                answer = f"Error, {num1} can not be divided by {num2}."
    return answer

