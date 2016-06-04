#! /usr/bin/python
import asana
import os
import sys
import json

wkspc_name = "Personal Projects"
access_token = os.environ.get('ASANA_PAT')
if access_token is None:
    print "ASANA_PAT environment var not set"
    sys.exit();

client = asana.Client.access_token(access_token)
(url, state) = client.session.authorization_url()
me = client.users.me()
print "Hello: " + me['name']
workspaces = me['workspaces']
wkspc_id = None
for wkspc in workspaces:
    if wkspc['name'] == wkspc_name:
        wkspc_id = wkspc['id']

if wkspc_id is None:
    print "Workspace not found"
    sys.exit()

projects = client.projects.find_by_workspace(wkspc_id)
for project in projects:
    print "Project: " + project['name']
    project_id = project['id'] 
    project_tasks = client.tasks.find_by_project(project_id)
#    for task in project_tasks:
#        print "  - " + str(task['id']) + task['name'] 
#        task_subtasks = client.tasks.subtasks(task['id'], full_payload=True)
#        for subtask in task_subtasks:
#            print "    + " + json.dumps(subtask, indent=2)
