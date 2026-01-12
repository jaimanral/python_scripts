def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculator():
    print("Choose operation: add, subtract, multiply, divide")
    operation = input("Operation: ").lower()
    a = float(input("First number: "))
    b = float(input("Second number: "))

    if operation == "add":
        print(add(a, b))
    elif operation == "subtract":
        print(subtract(a, b))
    elif operation == "multiply":
        print(multiply(a, b))
    elif operation == "divide":
        print(divide(a, b))
    else:
        print("Invalid operation")

if __name__ == "__main__":
    calculator()
