import re
from json_utils import read_all_data, save_data

def register():
    users = read_all_data("users.json")
    print("\n--- Register ---")

    while True:
        first_name = input("Enter First Name: ").strip()
        if first_name.isalpha():
            break
        print("Invalid first name!")

    while True:
        last_name = input("Enter Last Name: ").strip()
        if last_name.isalpha():
            break
        print("Invalid last name!")

    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    while True:
        email = input("Enter Email: ").strip()
        if not re.match(email_pattern, email):
            print("Invalid email format!")
            continue
        if any(user["email"] == email for user in users):
            print("Email already exists!")
        else:
            break

    while True:
        password = input("Enter Password: ")
        confirm = input("Confirm Password: ")
        if password == confirm and password:
            break
        print("Passwords do not match!")

    while True:
        phone = input("Enter Mobile Phone: ").strip()
        if phone.isdigit() and len(phone) == 11 and phone.startswith(("010","011","012","015")):
            break
        print("Invalid phone number!")

    new_user = {
        "id": len(users) + 1,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone
    }

    users.append(new_user)
    save_data("users.json", users)
    print("Registration successful!")

def login():
    users = read_all_data("users.json")
    print("\n--- Login ---")
    email = input("Enter Email: ").strip()
    password = input("Enter Password: ")

    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"Welcome {user['first_name']}!")
            return user
    print("Invalid email or password.")
    return None
