from arithmetic_operations import perform_operation

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (add/subtract/multiply/divide): ").strip().lower()

result = perform_operation(num1, num2, operation)

print(f"The result is: {result}")
