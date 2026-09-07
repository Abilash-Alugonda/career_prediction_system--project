import re

def validate_email(email): #email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))
def validate_phone(phone): #phone validaton
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, phone))
def validate_username(username):    #Create Username Validation
    pattern = r'^[A-Za-z0-9_]{3,20}$'
    return bool(re.match(pattern, username))
def validate_password(password):     #Create Password Validation
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
    return bool(re.match(pattern, password))
def validate_name(name):    #Create Name Validation
    pattern = r'^[A-Za-z ]{2,50}$'
    return bool(re.match(pattern, name.strip()))
def validate_age(age):  #Create Age Validation
    try:
        age = int(age)
    except (ValueError, TypeError):
        return False

    return 15 <= age <= 100
def validate_required(value):  #Create Required Field Validation
    return value is not None and str(value).strip() != ""

def validate_skills(skills):  #Create Skills Validation
    return isinstance(skills, list) and len(skills) > 0

def validate_interests(interests):   # Create Interests Validation
    return isinstance(interests, list) and len(interests) > 0

