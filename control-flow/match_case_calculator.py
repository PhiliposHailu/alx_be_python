num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        answer = num1 + num2
        print(f"The result is {answer}.")
    case "-":
        answer = num1 - num2
        print(f"The result is {answer}.")
    case "*":
        answer = num1 * num2
        print(f"The result is {answer}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            answer = num1 / num2
            print(f"The result is {answer}.")
    case _:
        print("The operator you entered don't match.Error!!!")

