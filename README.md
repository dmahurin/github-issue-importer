# Github Issue Importer
This repository created for import issues from csv file to Github repository.

# Requirements
- Python3
- Pip for python libraries

# Usage

### CSV File
To import issues you should create a csv file. You can find example csv file in the repository.

Example structure:

```
title;body;assignee;milestone;labels;
```

### Run
```
python3 main.py --token <GITHUB_TOKEN> --owner <REPO_OWNER> --name <REPO_NAME> --csvFile <CSV_FILE_PATH>
```
