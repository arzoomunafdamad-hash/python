def print_fibonacci(n):
    a, b = 0, 1

    print(f"Fibonacci series up to {n} terms:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Get user input
try:
    terms = int(input("Enter the number of terms: "))
    if terms <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        print_fibonacci(terms)
except ValueError:
    print("Invalid input. Please enter a valid integer.")