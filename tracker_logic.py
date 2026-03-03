import json
import os

FILE = "application.json"

def load_applications():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_applications(apps):
    with open(FILE, "w") as f:
        json.dump(apps, f, indent = 2)

def add_application(apps, company, role, date):
    app = {
        "company": company,
        "role": role,
        "date": date,
        "status": "Applied"
    }
    apps.append(app)
    return apps

def update_status(apps, index, new_status):
    if index < 0 or index >= len(apps):
        return None
    apps[index]["status"] = new_status
    return apps

def get_application(apps, index):
    if index < 0 or index >= len(apps):
        return None
    return apps[index]