import lib


def add(a, b):
    c = a + b
    return c


def sub(a, b):
    c = a - b
    return c


def mul(a, b):
    c = a * b
    return c


def div(a, b):
    c = a + b
    return c


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    """https: // www.geeksforgeeks.org / python - docstrings /
    Demonstrates triple double quotes
    docstrings and does nothing really."""
    print("Welcome to the Basic Calculator")
    print(lib.cal_logo)

    number1 = int(input("Enter the first number"))
    sym = input(f"Pick the operation '+', '-', '*', '/'")
    for sym in operations:
        print(sym)
    should_continue = True

    while should_continue:
        operation_symbol = sym
        number2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            number1 = answer
        else:
            should_continue = False


calculator()


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)


def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"


print(my_function(25))
