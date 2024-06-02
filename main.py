import json
import pandas as pd
import requests
import csv
import os
import time
import sys
import argparse

def xls_to_issues(xls_file):
    df = pd.read_excel(xls_file)

    issues = []

    for _, row in df.iterrows():
        issue = {
            "title": row["Task Name"],
            "body": row["Comments"] if "Comments" in row and row['Comments'] is str else '',
            "assignee": row["Assigned To"] if not pd.isna(row["Assigned To"]) else '',
        }
        issues.append(issue)
    return issues

def csv_to_issues(csvFile):
    issues = []

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
            issues.append(issue)
    return issues

def create_github_issue(data):
    # Add the issue to our repository
    curl = "curl -i -H 'Authorization: token %s' -d '%s' https://api.github.com/repos/%s/%s/issues" % (token, data, owner, name)
    os.system(curl)



parser = argparse.ArgumentParser()
parser.add_argument('--owner', help='Repo owner')
parser.add_argument('--name', help='Repo name')
parser.add_argument('--token', help='Github personal token')
parser.add_argument('--file', help='Issues File Path')
args = parser.parse_args()

if args.owner == None or args.name == None or args.token == None or args.file == None:
    print('Missing arguments')
    sys.exit()

owner = args.owner
name = args.name
token = args.token
issuesFile = args.file

if issuesFile.endswith('.csv'):
    issues = csv_to_issues(issuesFile)
elif issuesFile.endswith('.xlsx'):
    issues = xls_to_issues(issuesFile)
else:
    with open(csvFile, 'r', encoding='ISO-8859-1') as file:
        issues = json.load(file)

for issue in issues:
    if issue['assignee']:
        issue['assignee'] = ''
    data = json.dumps(issue)
    create_github_issue(data)
