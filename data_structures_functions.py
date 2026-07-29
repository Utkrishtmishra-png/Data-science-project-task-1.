"""
Week 2 - Hands-On Exercise: Data Structures and Functions
Concepts practiced: lists, tuples, dictionaries, sets, functions,
lambda functions, recursion, and list comprehension.
"""


# ---------- Lists, Tuples, Dictionaries, Sets ----------

def demo_data_structures():
    print("--- Lists, Tuples, Dictionaries, Sets ---")

    # List: ordered, mutable
    fruits = ["apple", "banana", "cherry", "apple"]
    fruits.append("date")
    print("List:", fruits)

    # Tuple: ordered, immutable — good for fixed records like coordinates
    point = (10, 20)
    print("Tuple:", point)

    # Dictionary: key-value pairs
    student_scores = {"Alice": 92, "Bob": 78, "Chen": 85}
    student_scores["Diego"] = 88
    print("Dictionary:", student_scores)

    # Set: unordered, unique elements — great for de-duplication
    unique_fruits = set(fruits)
    print("Set (duplicates removed):", unique_fruits)
    print()


# ---------- Functions for Data Transformation ----------

def sum_of_squares(numbers):
    """Return the sum of squares of a list of numbers."""
    total = 0
    for n in numbers:
        total += n ** 2
    return total


def filter_even(numbers):
    """Return only the even numbers from a list, using list comprehension."""
    return [n for n in numbers if n % 2 == 0]


def filter_above_threshold(records, key, threshold):
    """Generic filter: keep dict records where record[key] > threshold."""
    return [r for r in records if r.get(key, 0) > threshold]


# ---------- Lambda Functions ----------

square = lambda x: x ** 2
is_positive = lambda x: x > 0


def demo_lambdas(numbers):
    print("--- Lambda Functions ---")
    squared = list(map(square, numbers))
    positives = list(filter(is_positive, numbers))
    print(f"Original: {numbers}")
    print(f"Squared (map + lambda): {squared}")
    print(f"Positives (filter + lambda): {positives}")

    # sorting with a lambda key
    words = ["banana", "kiwi", "apple", "fig"]
    words_by_length = sorted(words, key=lambda w: len(w))
    print(f"Words sorted by length: {words_by_length}")
    print()


# ---------- Recursion ----------

def factorial(n):
    """Classic recursion example: n! = n * (n-1)!"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Return the nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def demo_recursion():
    print("--- Recursion ---")
    print(f"5! = {factorial(5)}")
    fib_sequence = [fibonacci(i) for i in range(10)]  # list comprehension too
    print(f"First 10 Fibonacci numbers: {fib_sequence}")
    print()


# ---------- List Comprehension ----------

def demo_list_comprehension():
    print("--- List Comprehension ---")
    numbers = list(range(1, 11))

    squares = [n ** 2 for n in numbers]
    even_squares = [n ** 2 for n in numbers if n % 2 == 0]
    pairs = [(n, n ** 2) for n in numbers if n % 3 == 0]

    print(f"Numbers: {numbers}")
    print(f"Squares: {squares}")
    print(f"Even squares only: {even_squares}")
    print(f"(n, n^2) pairs for multiples of 3: {pairs}")
    print()


def main():
    demo_data_structures()

    numbers = [-4, -1, 0, 2, 3, 5, 8]
    print("--- Functions for Data Transformation ---")
    print(f"Numbers: {numbers}")
    print(f"Sum of squares: {sum_of_squares(numbers)}")
    print(f"Even numbers: {filter_even(numbers)}")

    records = [
        {"name": "Alice", "score": 92},
        {"name": "Bob", "score": 65},
        {"name": "Chen", "score": 78},
    ]
    print(f"Records above 70: {filter_above_threshold(records, 'score', 70)}")
    print()

    demo_lambdas(numbers)
    demo_recursion()
    demo_list_comprehension()


if __name__ == "__main__":
    main()
