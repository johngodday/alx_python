#!user/bin/python3
def validate_password(password):
    if len(password) <  8:
        return False
    
    upper_check = False
    lower_check = False
    digit_check = False

    for i in password:
        if i.isupper():
            upper_check = True
        elif i.islower():
            lower_check = True
        elif i.isdigit():
            digit_check = True
        

    if not (upper_check and lower_check and digit_check):
        return False
    
    if " " in password:
        return False
    
    return True
