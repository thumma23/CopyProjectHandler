import auth_token
import gitlab
import requests
import time
import json

## Auth token is file in directory tha contains the private token credentiels required to
# authenticate into server
# Stored in "private_tok" dictionary 

class gl_project():
    def __init__(self, domain_name):
        ## Domain name of gitlab
        self.domain_name = domain_name

    ## group_name - Name of group to create project in
    ## new_project - Name of new project to create
    def create_newproject(self, group_name, new_project):
        # Authenticates user
        r = gitlab.Gitlab(self.domain_name , private_token= auth_token.private_tok['Token'])
        # Create project
        # Get project ID
        group_id = r.groups.list(search=group_name)[0].id
        # Create project within specified group
        project = r.projects.create({'name': new_project, 'namespace_id': group_id}) 
    
    ## _id - ID of project user wants to copy
    def archive_project(self, _id):
        ## Params = Domain name, Project ID, branch to copy
        archive_project = requests.get(f"{self.domain_name}/api/v4/projects/{_id}/repository/archive?sha=master", headers = {'PRIVATE-TOKEN' : auth_token.private_tok['Token']})
        ##Archive project contains content of file
        ## read arhcive_project into archive.zip
        ## archive.zip is stored in local dir

        with open('archive.zip', 'wb') as f:
            for chunk in archive_project.iter_content(chunk_size=128):
                f.write(chunk)
        time.sleep(10)


    ## push_branch - Branch of new project to push copied project to
    ## file_action - either create, delete or update
    def push_project(self, new_project, push_branch, file_action):
        ## Get project ID
        r = gitlab.Gitlab(self.domain_name, private_token= auth_token.private_tok['Token'])
        project_id = r.projects.list(search=new_project)[0].id
        ## PAYLOAD : specifies content of commit
        ## Includes branch to push to, commit message and action as per file
        payload = {
            "branch": push_branch,
            "commit_message": "test api commit 3",
            "actions": [
                {
                "action": file_action, 
                "file_path": "archive.zip",
                "content" : open('archive.zip', 'wb'),
                }
            ]
        }
        print(payload)
        ## Content type must be in json in order to facilitate the PAYLOD param
        headers = {
            'PRIVATE-TOKEN' : auth_token.private_tok['Token'],
            'Content-Type' : 'application/json'
        }

        commit_to_gitlab = requests.post(f"{self.domain_name}/api/v4/projects/{project_id}/repository/commits", headers = headers, json = payload )
        print("*****DONE", commit_to_gitlab)
