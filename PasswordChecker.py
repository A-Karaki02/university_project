import re

pattern = re.compile(
    r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&*!-+=()])(?=\S+$).{8,}$"
)


def password_check(password):
    if re.match(pattern, password):
        print("Valid password")
        return True
    else:
        print("Invalid password. Please ensure it meets the following criteria:")
        print("- At least 8 characters long")
        print("- Contains at least one digit (0-9)")
        print("- Contains at least one lowercase letter (a-z)")
        print("- Contains at least one uppercase letter (A-Z)")
        print("- Contains at least one special character (@#$%^&*!-+=())")
        print("- No whitespace characters allowed")
        return False
