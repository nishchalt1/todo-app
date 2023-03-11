password = input("Enter the password:")


def strength(password):
    result = []

    if len(password) >= 8:
        result.append(True)
    else:
        result.append(False)

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result.append(digit)

    upper_case = False
    for i in password:
        if i.isupper():
            upper_case = True

    result.append(upper_case)
    return all(result)


if strength_password(password) == True:
    print("Strong Password.")
else:
    print("Weak Password.")






