import json
import requests
import csv
import os
import time
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--owner', help='Repo owner')
parser.add_argument('--name', help='Repo name')
parser.add_argument('--token', help='Github personal token')
parser.add_argument('--csvFile', help='CSV File Path')
args = parser.parse_args()

if args.owner == None or args.name == None or args.token == None or args.csvFile == None:
    print('Missing arguments')
    sys.exit()

owner = args.owner
name = args.name
token = args.token
csvFile = args.csvFile

def create_github_issue(data):
    # Add the issue to our repository
    curl = "curl -i -H 'Authorization: token %s' -d '%s' https://api.github.com/repos/%s/%s/issues" % (token, data, owner, name)
    os.system(curl)

with open(csvFile, 'r', encoding='ISO-8859-1') as file:
    reader = csv.DictReader(file, delimiter=';')

    for row in reader:
        title = row['title']
        body = row['body']
        assignee = row['assignee']
        milestone = row['milestone']
        labels = [row['labels']]

        if row['assignee'] == 'None':
            assignee = None
        if row['body'] == 'None':
            body = None
        if row['milestone'] == 'None':
            milestone = None
        if row['labels'] == 'None':
            labels = []

        issue = {
             'title': title,
             'body': body,
             'assignee': assignee,
             'milestone': milestone,
             'labels': labels
        }

        data = json.dumps(issue)
        create_github_issue(data)
