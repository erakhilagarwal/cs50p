from validator_collection import checkers

def main():
    print(validate_email(input("What's your email address? ")))


def validate_email(email):
    if checkers.is_email(email):
        return "Valid"
    return "Invalid"


if __name__ == "__main__":
    main()