from backend.json_handler import load_profiles, save_profiles
from backend.validation import (
    validate_name,
    validate_age,
    validate_required,
    validate_skills,
    validate_interests
)


def profile_exists(user_id):
    profiles = load_profiles()

    for profile in profiles:
        if profile["user_id"] == user_id:
            return True

    return False


def create_profile(
    user_id,
    name,
    age,
    education,
    degree,
    branch,
    skills,
    experience,
    interests,
    preferred_career,
    certifications
):

    # Validate name
    if not validate_name(name):
        raise ValueError("Invalid name")

    # Validate age
    if not validate_age(age):
        raise ValueError("Invalid age")

    # Validate required fields
    if not validate_required(education):
        raise ValueError("Education is required")

    if not validate_required(degree):
        raise ValueError("Degree is required")

    if not validate_required(branch):
        raise ValueError("Branch is required")

    # Validate skills
    if not validate_skills(skills):
        raise ValueError("At least one skill is required")

    # Validate interests
    if not validate_interests(interests):
        raise ValueError("At least one interest is required")

    # Validate career
    if not validate_required(preferred_career):
        raise ValueError("Preferred career is required")

    # Check duplicate profile
    if profile_exists(user_id):
        raise ValueError("Profile already exists")

    profile = {
        "user_id": user_id,
        "name": name,
        "age": int(age),
        "education": education,
        "degree": degree,
        "branch": branch,
        "skills": skills,
        "experience": experience,
        "interests": interests,
        "preferred_career": preferred_career,
        "certifications": certifications
    }

    profiles = load_profiles()
    profiles.append(profile)

    save_profiles(profiles)

    return profile
def get_profile(user_id):    #  Add Profile Retrieval

    profiles = load_profiles()

    for profile in profiles:
        if profile["user_id"] == user_id:
            return profile

    raise ValueError("Profile not found")

def update_profile(user_id, updated_data):    # Add Profile Update

    profiles = load_profiles()

    for profile in profiles:

        if profile["user_id"] == user_id:

            profile.update(updated_data)

            save_profiles(profiles)

            return profile

    raise ValueError("Profile not found")


