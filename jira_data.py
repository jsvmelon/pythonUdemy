from atlassian import Jira
import requests
import base64
import json

file = open("/home/js/code/JiraToken", "r")
JIRA_TOKEN = file.readline()[:-1]  # remove the trailing newline character
USER = "jean-sacha.melon@smarkets.com"
URL = """https://notsmarkets.atlassian.net/"""

jira_instance = Jira(url=URL, username=USER, password=JIRA_TOKEN)

# json_jira = jira_instance.issue(key="TFI-31")
jira_instance.issue_create(
    fields={
        "project": {"key": "TFI"},
        "issuetype": {"name": "Task"},
        "summary": "created with python",
        "description": "whatever suits you",
    })


