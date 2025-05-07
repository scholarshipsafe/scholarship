import json

def load_scholarships(filename="scholarships.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data["scholarships"]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON.")
        return []

def display_scholarships(scholarships):
    if not scholarships:
        print("No scholarships available.")
        return

    print("Available Scholarships:\n")
    for idx, scholarship in enumerate(scholarships, start=1):
        print(f"{idx}. {scholarship['name']}")
        print(f"   Amount: {scholarship['amount']}")
        print(f"   Deadline: {scholarship['deadline']}")
        print(f"   URL: {scholarship['url']}\n")

if __name__ == "__main__":
    scholarships = load_scholarships()
    display_scholarships(scholarships)
