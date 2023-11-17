

def check_creds(cred):
    if "password" in cred and "getpass" not in cred:
        return True
    elif "username" in cred and "input(" not in cred:
        return True
    else:
        return False


def main():
    with open("Calc.py", "r") as calc:
        code = calc.read()

    for line in code.split("\n"):
        if "password" in line or "username" in line:
            if check_creds(line):
                return True

    return False