import re



# Utility function for validating email format
def is_valid_email(email):
    # A simple regex to validate email format
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(regex, email))

# Utility function to validate phone number (simple check for digits)
def is_valid_phone_number(phone_number):
    return phone_number.isdigit() and len(phone_number) == 10

# Utility function for validating if an input is a valid number (used for cost or amount)
def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Utility function to safely get input from the user
def safe_input(prompt, validation_func=None, error_message="Invalid input. Please try again."):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty.")
            continue
        if validation_func and not validation_func(user_input):
            print(error_message)
        else:
            return user_input

# Utility function to format currency (for cost or transaction amounts)
def format_currency(amount):
    return "${:,.2f}".format(amount)

# Utility function to confirm user actions (Yes/No)
def confirm_action(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print("Please answer with 'yes' or 'no'.")
