import os
import yaml

with open('TableOfContents.yml', 'r') as file:
    projects = yaml.safe_load(file)

# Check if 'Projects' key exists in the YAML file
if isinstance(projects, list):
    for project_data in projects:
        project = project_data.get('Project', {})
        project_number = project.get('Number')
        project_title = project.get('Title')

        # Skip projects without 'Number' or 'Title' keys
        if project_number is None or project_title is None:
            print(f"Skipping invalid project: {project}")
            continue

        folder_name = f"{project_number}_{project_title.replace(' ', '_')}"
        os.makedirs(folder_name, exist_ok=True)

        with open(f"{folder_name}/README.md", 'w') as readme_file:
            readme_file.write(
                f"# {project_title} ({project_number})\n\nDifficulty: {project.get('Difficulty', 'Unknown')}\n\n{project.get('Description', 'No description provided')}")

        with open(f"{folder_name}/{folder_name}.py", 'w') as code_file:
            code_file.write("# Write your code here")
else:
    print("Invalid YAML file format. Please ensure that the 'Projects' key is present.")
