from email_validator import validate_email, EmailNotValidError
import phonenumbers

def emailValidator(data):
    try:
        valid = validate_email(data["email"])
        email = valid.normalized
    except EmailNotValidError as e:
        return None, (f"Invalid email: {e}")
    else:
        return email, None

def phoneValidator(data):
    try:
        number = phonenumbers.parse(data["phoneNumber"], "GB")
        if not phonenumbers.is_valid_number(number):
            raise ValueError("Invalid Phone Number")
        formatted = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
    except(phonenumbers.NumberParseException, ValueError):
        return None, "Invalid phone number"
    else:
        return formatted, None
