import json
import os

USERS_FILE = "data/users.json"
PROFILES_FILE = "data/user_profiles.json"
def load_json(filename):     #Create a JSON Reading Function
    try:
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []

    except OSError as e:
        raise RuntimeError(f"Error reading file: {e}")
def save_json(filename, data):    #Create a JSON Writing Function
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    except OSError as e:
        raise RuntimeError(f"Error writing file: {e}")
def load_users():    #Create User-Specific Functions
    return load_json(USERS_FILE)


def save_users(users):
    save_json(USERS_FILE, users)


def load_profiles():   # add for  profiles
    return load_json(PROFILES_FILE)


def save_profiles(profiles):
    save_json(PROFILES_FILE, profiles)
    