"""
Week 1 - Hands-On Exercise: Temperature Converter
Concepts practiced: variables, data types, operators, input/output,
conditional statements (if-elif-else), and loops (while).

The program repeatedly asks the user to convert a temperature between
Celsius, Fahrenheit, and Kelvin until they choose to quit.
"""


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def celsius_to_kelvin(c):
    return c + 273.15


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def kelvin_to_celsius(k):
    return k - 273.15


def print_menu():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Kelvin to Celsius")
    print("5. Quit")


def get_float(prompt):
    """Keep asking until the user enters a valid number (basic input validation)."""
    while True:
        raw_value = input(prompt)
        try:
            return float(raw_value)
        except ValueError:
            print("Please enter a valid number.")


def main():
    running = True  # loop control variable

    while running:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            c = get_float("Enter temperature in Celsius: ")
            print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
        elif choice == "2":
            c = get_float("Enter temperature in Celsius: ")
            print(f"{c}°C = {celsius_to_kelvin(c):.2f}K")
        elif choice == "3":
            f = get_float("Enter temperature in Fahrenheit: ")
            print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
        elif choice == "4":
            k = get_float("Enter temperature in Kelvin: ")
            print(f"{k}K = {kelvin_to_celsius(k):.2f}°C")
        elif choice == "5":
            print("Goodbye!")
            running = False
        else:
            print("Invalid option, please choose 1-5.")


if __name__ == "__main__":
    main()
