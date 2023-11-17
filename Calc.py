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
    username = input("Enter username: ")
    password = getpass.getpass()
    multiplication(2, 3)

