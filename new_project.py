import yaml

# Load existing projects from the YAML file
with open('TableOfContents.yml', 'r') as file:
    existing_projects = yaml.safe_load(file)

# Prompt user for new project details
new_title = input("Enter the project title: ")
new_difficulty = input("Enter the difficulty (Easy | Medium | Hard | FML): ")
new_description = input("Enter the project description: ")
new_contributor = input("Enter the project contributor: ")

# Determine the new project number
if existing_projects:
    last_project_number = int(existing_projects[-1]['Project']['Number'])
    new_project_number = str(last_project_number + 1).zfill(3)
else:
    new_project_number = "001"

# Create the new project dictionary
new_project = {
    'Project': {
        'Number': new_project_number,
        'Title': new_title,
        'Difficulty': new_difficulty,
        'Contributor': new_contributor,
        'Description': new_description
    }
}

# Append the new project to the existing projects
existing_projects.append(new_project)

# Write the updated projects back to the YAML file
with open('TableOfContents.yml', 'w') as file:
    yaml.dump(existing_projects, file, default_flow_style=False)

print(f"Project '{new_title}' added successfully with number {new_project_number}.")
