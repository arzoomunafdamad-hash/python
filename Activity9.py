def f(number):
    fact = 1
    for i in range(1, number+1):
        fact = fact*i
    print("the factorial of a given number is", fact)

number = int(input("Enter a number: "))
f(number)