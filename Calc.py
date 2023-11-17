# Calculator
import getpass


def addition(x, y):
    result = x + y
    return result


def subtraction(x, y):
    result = x - y
    return result


def division(x, y):
    result = x / y
    return result


def multiplication(x, y):
    result = x * y
    return result


def main():
    multiplication(2, 3)


if __name__ == '__main__':
    username = input()
    password = getpass.getpass()
    main()
