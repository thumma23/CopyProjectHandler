from gitlab_copy_project_handler import gl_project
import auth_token

obj = gl_project("http://git.home.stacklynx.com", auth_token.private_tok['Token'])

obj.archive_project(19)