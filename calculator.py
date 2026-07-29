"""
Week 1 - Hands-On Exercise: Basic Calculator
Concepts practiced: variables, data types, operators (+, -, *, /, //, %, **),
input/output, conditional statements, and loops (while, for).
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


def power(a, b):
    return a ** b


def modulo(a, b):
    if b == 0:
        return "Error: division by zero"
    return a % b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "%": modulo,
}


def get_number(prompt):
    while True:
        raw_value = input(prompt)
        try:
            return float(raw_value)
        except ValueError:
            print("That's not a number, try again.")


def main():
    print("--- Basic Calculator ---")
    print(f"Supported operators: {', '.join(OPERATIONS.keys())}")

    calculations_done = 0  # counter, demonstrates a running total across loop iterations

    while True:
        num1 = get_number("Enter the first number: ")
        op = input("Enter an operator (or 'q' to quit): ").strip()

        if op.lower() == "q":
            break

        if op not in OPERATIONS:
            print("Unsupported operator, please try again.")
            continue

        num2 = get_number("Enter the second number: ")
        result = OPERATIONS[op](num1, num2)
        print(f"Result: {num1} {op} {num2} = {result}")
        calculations_done += 1

    print(f"\nSession summary: you performed {calculations_done} calculation(s). Goodbye!")


if __name__ == "__main__":
    main()
