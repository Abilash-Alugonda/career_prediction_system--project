from backend.validation import (
    validate_email,
    validate_phone,
    validate_username,
    validate_password,
    validate_name,
    validate_age,
    validate_required,
    validate_skills,
    validate_interests
)


print("EMAIL TESTS")
print(validate_email("abilash@gmail.com"))
print(validate_email("abilashgmail.com"))

print("\nPHONE TESTS")
print(validate_phone("9876543210"))
print(validate_phone("12345"))

print("\nUSERNAME TESTS")
print(validate_username("abilash_123"))
print(validate_username("ab@123"))

print("\nPASSWORD TESTS")
print(validate_password("Abilash@123"))
print(validate_password("12345"))

print("\nNAME TESTS")
print(validate_name("Abilash Reddy"))
print(validate_name("Abilash123"))

print("\nAGE TESTS")
print(validate_age(22))
print(validate_age(10))

print("\nREQUIRED FIELD TESTS")
print(validate_required("Abilash"))
print(validate_required(""))

print("\nSKILLS TESTS")
print(validate_skills(["Python", "SQL"]))
print(validate_skills([]))

print("\nINTEREST TESTS")
print(validate_interests(["AI", "Data Science"]))
print(validate_interests([]))