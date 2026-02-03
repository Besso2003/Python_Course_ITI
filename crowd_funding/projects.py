import re
from json_utils import read_all_data, save_data
from datetime import datetime

def create_project(current_user):
    projects = read_all_data("projects.json")
    print("\n--- Create Project ---")

    title = input("Enter Project Title: ").strip()
    details = input("Enter Project Details: ").strip()

    while True:
        target = input("Enter Total Target (EGP): ").strip()
        if target.isdigit() and int(target) > 0:
            target = int(target)
            break
        print("Invalid amount! Please enter a positive number.")

    date_format = "%Y-%m-%d"
    while True:
        start_date = input("Enter Start Date (YYYY-MM-DD): ").strip()
        end_date = input("Enter End Date (YYYY-MM-DD): ").strip()
        try:
            start_dt = datetime.strptime(start_date, date_format)
            end_dt = datetime.strptime(end_date, date_format)
            if end_dt <= start_dt:
                print("End date must be after start date!")
                continue
            break
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD.")

    new_project = {
        "id": len(projects) + 1,
        "user_id": current_user["id"],
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date
    }

    projects.append(new_project)
    save_data("projects.json", projects)
    print("Project created successfully!")


def view_projects():
    projects = read_all_data("projects.json")
    if not projects:
        print("No projects found.")
        return

    print("\n--- All Projects ---")
    for project in projects:
        print(f"\nID: {project['id']}")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Target: {project['target']} EGP")
        print(f"Start Date: {project['start_date']}")
        print(f"End Date: {project['end_date']}")


def edit_project(current_user):
    projects = read_all_data("projects.json")
    user_projects = [p for p in projects if p["user_id"] == current_user["id"]]

    if not user_projects:
        print("You have no projects to edit.")
        return

    print("\n--- Your Projects ---")
    for project in user_projects:
        print(f"ID: {project['id']}, Title: {project['title']}")

    while True:
        proj_id = input("Enter the Project ID to edit: ").strip()
        if proj_id.isdigit():
            proj_id = int(proj_id)
            project = next((p for p in user_projects if p["id"] == proj_id), None)
            if project:
                break
        print("Invalid Project ID! Please try again.")

    new_title = input(f"Enter new Title [{project['title']}]: ").strip() or project['title']
    new_details = input(f"Enter new Details [{project['details']}]: ").strip() or project['details']

    while True:
        new_target = input(f"Enter new Target (EGP) [{project['target']}]: ").strip() or str(project['target'])
        if new_target.isdigit() and int(new_target) > 0:
            new_target = int(new_target)
            break
        print("Invalid amount! Please enter a positive number.")

    project["title"] = new_title
    project["details"] = new_details
    project["target"] = new_target

    save_data("projects.json", projects)
    print("Project updated successfully!")


def delete_project(current_user):
    projects = read_all_data("projects.json")
    user_projects = [p for p in projects if p["user_id"] == current_user["id"]]

    if not user_projects:
        print("You have no projects to delete.")
        return

    print("\n--- Your Projects ---")
    for project in user_projects:
        print(f"ID: {project['id']}, Title: {project['title']}")

    while True:
        proj_id = input("Enter the Project ID to delete: ").strip()
        if proj_id.isdigit():
            proj_id = int(proj_id)
            project = next((p for p in user_projects if p["id"] == proj_id), None)
            if project:
                break
        print("Invalid Project ID! Please try again.")

    projects.remove(project)
    save_data("projects.json", projects)
    print("Project deleted successfully!")


def search_projects():
    projects = read_all_data("projects.json")
    if not projects:
        print("No projects found.")
        return
    
    date_format = "%Y-%m-%d"
    date_input = input("Enter a date to search projects (YYYY-MM-DD): ").strip()
    try:
        dt = datetime.strptime(date_input, date_format)
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")
        return
    
    found = [p for p in projects if p["start_date"] <= date_input <= p["end_date"]]
    if not found:
        print("No projects found on this date.")
        return

    print("\n--- Projects on Date ---")
    for project in found:
        print(f"\nID: {project['id']}")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Target: {project['target']} EGP")
        print(f"Start Date: {project['start_date']}")
        print(f"End Date: {project['end_date']}")