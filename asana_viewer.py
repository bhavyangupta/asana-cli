#! /usr/bin/python
import asana
import string
import os
import sys, getopt
import json
import textwrap

def usage():
  print "Usage: asana_viewer -w <wkspc> -p <project>"
  sys.exit()

try:
  (opts, args) = getopt.getopt(sys.argv[1:], "hw:p:o:")
except getopt.GetoptError:
  usage()

wkspc_name = None
project_name = None
for opt, arg in opts:
  if opt == '-w':
    wkspc_name = arg
  elif opt == '-p':
    project_name = arg
  elif opt == '-h':
    usage()

if wkspc_name is None or project_name is None:
  usage()
print "Workspace: %s | Project: %s" % (wkspc_name, project_name)

# Login
access_token = os.environ.get('ASANA_PAT')
if access_token is None:
    print "ASANA_PAT environment var not set"
    sys.exit();

client = asana.Client.access_token(access_token)
(url, state) = client.session.authorization_url()
me = client.users.me()

# Find the right workspace
wkspc_id = None
for workspace in me['workspaces']:
    if workspace['name'] == wkspc_name:
        wkspc_id = workspace['id']

if wkspc_id is None:
    print "Workspace doesn't exist"
    sys.exit()

# Find the right project
project_id = None
for project in client.projects.find_by_workspace(wkspc_id):
    if project['name'] == project_name:
        project_id = project['id']
if project_id is None:
    print "Project doesn't exist"
    sys.exit()

#project = asana.resources.projects.Projects(client)
#manifest =  project.find_by_id(project_id)
#
## Display project tasks
task = asana.resources.tasks.Tasks(client)
tasklist = task.find_by_project(project_id, {"opt_fields":"name,completed,assignee,tags"})
header_str = "Description | Status | Tags | Assigned To"
separator = "----------------------------------------"
print header_str
print separator
for t in tasklist:
    if not t['completed']:
        assignee = 'None'
        if t['assignee'] is not None:
            assignee = client.users.find_by_id(t['assignee']['id'])['name']
        assignee = assignee.ljust(10)
        names = textwrap.wrap(t['name'],40)
        name = [name.ljust(40) for name in names] 
        name = "\n".join(name)
        completed = str(t['completed']).ljust(6)
        tags = str(t['tags']).ljust(10)
        entry =  "%s | %s | %s | %s" % (name, completed, tags, assignee) 
        print entry
        print "-------------------------------------------------------------"

