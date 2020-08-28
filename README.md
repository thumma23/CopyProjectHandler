This program allows the user to create a project within a specified group, copy a selected project and past the copied project into the newly created project all via github.

The first method - create_newobject - requires two parameters: group_name and new_project and creates a new project in a selected group
  group_name : name of the group that the user wants to create the project in
  new_project : name of new project to create

The second method - archive_project - requires one parameter: id and archives the selected project into the user's local workspace
  id : id of project user wants to copy
  
The third method - push_project - requires three parameters: new_project, push_branch, file_action and pushes the archived project to a selected project group
  new_project : project name of where user wants to push the copied file to
  push_branch : name of branch where the user wants to push changes
  file_action : action user chooses to do, options are: "create", "update", and "delete"
  
  How to Use - 
    Create class object with domain name and private token parameters and call selected method.
    Eg:
    
    Domain name = 123.com
    private token = 'abc'
    
    *****************************
    
    from gitlab import gl_project
    
    gl_project_obj = gl_project('123.com' , 'abc')
    // to call method
    gl_project_obj.create_new_project(*params*)
    
  
