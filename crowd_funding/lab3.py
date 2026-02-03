from auth import register, login
from projects import create_project, view_projects, edit_project, delete_project, search_projects

current_user = None

while True:
    if not current_user:
        print("\n===== Crowd Funding APP =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            current_user = login()
            if current_user:
                print(f"\nWelcome {current_user['first_name']}! You can now manage projects.")
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
    else:
        print(f"\n===== Project Menu (Logged in as {current_user['first_name']}) =====")
        print("1. Create Project")
        print("2. View Projects")
        print("3. Edit Project")
        print("4. Delete Project")
        print("5. Search Projects by Date")
        print("6. Logout")

        choice = input("Choose an option: ")

        if choice == '1':
            create_project(current_user)
        elif choice == '2':
            view_projects()
        elif choice == '3':
            edit_project(current_user)
        elif choice == '4':
            delete_project(current_user)
        elif choice == '5':
            search_projects()
        elif choice == '6':
            print(f"Logging out {current_user['first_name']}...")
            current_user = None
        else:
            print("Invalid option. Please try again.")
