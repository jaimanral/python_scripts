def check_password_strength(password):
    if len(password) < 8:
        return "Weak password"

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if has_upper and has_lower and has_digit:
        return "Strong password"
    return "Medium password"

if __name__ == "__main__":
    pwd = input("Enter password: ")
    print(check_password_strength(pwd))
