#key for lab 7
#password must have at least 10 characters
#password must contain at least one UPPER case letter
#password must contain at least one SPECIAL character !@#$%^&*()

#1. PROMPTS THE USER TO ENTER A PASSWORD
#2. DISPLAYS VALID PASSWORD IF RULES ARE TRUE
    #INVALID if false
#3. Use a function when writing
    #Two sample runs

def valid_password(password):
    #Boolean logic
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_isspace = False

    if len(password) >=10:
        correct_length = True
    #if len(spec_char) == ['!@#$%^&*()?+=']

        #special character =
    for ch in password:
        if ch.isupper():
            has_uppercase = True
        if ch.islower():
            has_lowercase = True
        if ch.isdigit():
            has_digit = True
        if ch.isspace():
            has_isspace = True
           
    if correct_length and has_uppercase and has_lowercase and has_digit and \
       has_isspace:
        is_valid = True
    else:
            is_valid = False

    return is_valid
       
