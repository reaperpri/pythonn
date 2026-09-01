import re
#Email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False
def validate_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    if re.match(pattern, password):
        return True
    else:
        return False    
def validate_phone_number(phone_number):
    pattern = r'^\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False
#test
email = "test@gmail.com"
password = "makhan@99!"
phone_number = "+91-9876543210"
print("Email validation result:", validate_email(email))
print("Password validation result:", validate_password(password))
print("Phone number validation result:", validate_phone_number(phone_number))