#! /usr/bin/python3
import yaml
import os



def create_readme(item_dictionary):
    readme = "# Coding Prompt "
    readme = readme + str(item_dictionary['Number']) + ' • ' + item_dictionary['Title'] + '\n \n'
    readme = readme + "### Difficulty: " + item_dictionary['Difficulty'] + '\n \n'
    readme = readme + item_dictionary['Description']
    foldername = str(item_dictionary['Number']) + ' - ' + item_dictionary['Title']
    # print(readme)
    # print(foldername)
    return readme, foldername


parent_dir = os.path.dirname(__file__)
all_projects_dir = os.path.join(parent_dir, 'prompts/')

if __name__ == '__main__':
    project_list = []
    with open(os.path.join(parent_dir,"TableOfContents.yml"), 'r') as stream:
        thelist = yaml.safe_load(stream)
    for x in range(0, len(thelist)):
        item = thelist[x]['Project']
        readme, foldername = create_readme(item)
        project_dir = os.path.join(all_projects_dir, foldername)
        try:
            os.mkdir(all_projects_dir)
            os.mkdir(project_dir)
        except:
            os.system("rm -Rf '%s'" % project_dir)
            os.mkdir(project_dir)
        readme_location=os.path.join(project_dir, "readme.md")
        try:
            with open(readme_location, "w+") as text_file:
                text_file.write(readme)
        except:
            os.system("rm -Rf '%s'" % project_dir)
            os.mkdir(project_dir)
            with open(readme_location, "w+") as text_file:
                text_file.write(readme)
