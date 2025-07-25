num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = str(input ("Choose the operation (+ ,- , * , / )"))

match operation:
    case "+":
        print ("The result is {}".format(num1 + num2))
    case "-":
        print ("The result is {}".format(num1 - num2))
    case "*":
        print ("The result is {}".format(num1 *num2))
    case "/":
        print ("The result is{}".format(num1 / num2))
    case _:
        print("Cannot divide by zero")
        






