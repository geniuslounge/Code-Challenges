#! /usr/bin/python3
import yaml
import os
# BEGIN KEYBASE SALTPACK SIGNED MESSAGE. kXR7VktZdyH7rvq v5weRa0zkCKQFII gl3XdhOkQjlE9nf 0X3j7bWfBrt5UVh H99I2RmyMiwG3um JQF0Tsn0zc86jb3 dBAeUfnLOmrjQQW DAmkE035ONKunFe 22GlRoejpQkxw6W PhKyTWPgVjzsnTq VWXBonGdZ2l7a7g Zjfm1C033cHiWIE iF2GlMndusUYqUT Py4KpTN75z5YNB. END KEYBASE SALTPACK SIGNED MESSAGE.

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
all_projects_dir = os.path.join(parent_dir, 'projects/')

if __name__ == '__main__':
    project_list = []
    with open(os.path.join(parent_dir,"TableOfContents.yml"), 'r') as stream:
        thelist = yaml.safe_load(stream)
    for x in range(0, len(thelist)):
        item = thelist[x]['Project']
        readme, foldername = create_readme(item)
        project_dir = os.path.join(all_projects_dir, foldername)
        try:
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
