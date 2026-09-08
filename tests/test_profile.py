from backend.user_profile import create_profile, get_profile


profile = create_profile(
    "USR001",
    "Abilash Reddy",
    22,
    "B.Tech",
    "Computer Science",
    "CSE",
    ["Python", "SQL", "Java"],
    0,
    ["AI", "Web Development"],
    "Software Developer",
    ["Python Certification"]
)

print("Profile created successfully!")
print(profile)


print("\nGetting Profile...")

result = get_profile("USR001")

print(result)