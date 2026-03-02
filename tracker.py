import json
import os

FILE = "applications.json"

def load_applications():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []
    
def save_applications(apps):
    with open(FILE, "w") as f:
        json.dump(apps, f, indent=2)

def add_application(apps):
    company = input("Company name: ")
    role = input("Role/Position: ")
    date = input("Data applied (MM/DD/YYYY):")
    app = {
        "company": company,
        "role": role,
        "date": date,
        "status": "Applied"
    }
    apps.append(app)
    save_applications(apps)
    print("Application added successfully!\n")

def view_applications(apps):
    if not apps:
        print("No applications yet.\n")
        return
    print("\n--- Your Applications ---")
    for i, app in enumerate(apps):
        print(f"{i+1}. {app['company']} | {app['role']} | {app['date']} | {app['status']}")
    print()

def update_status(apps):
    view_applications(apps)
    if not apps:
        return
    index = int(input("Enter application number to update: ")) - 1
    print("Statuses: Applied, Interview, Offer, Rejected")
    new_status = input("New status: ")
    apps[index]["status"] = new_status
    save_applications(apps)
    print("Status updated!\n")

def main():
    apps = load_applications()
    while True:
        print("=== Job Application Tracker ===")
        print("1. Add application")
        print("2. View applications")
        print("3. Update status")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_application(apps)
        elif choice == "2":
            view_applications(apps)
        elif choice == "3":
            update_status(apps)
        elif choice == "4":
            print("Good luck out there!")
            break
        else:
            print("Invalid option, try again.\n")

main()