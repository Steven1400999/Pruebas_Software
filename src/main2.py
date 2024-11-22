def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    if y == 0:
        return ZeroDivisionError("Cannot divide by zero")
    return x / y
