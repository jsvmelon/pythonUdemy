from atlassian import Jira
import pprint


def get_jira_instance():
    """
    Constructs an instance of the Atlassian Jira object to easily access Jira
    via the API.
    :return: instance of the Atlassian Jira object
    """
    file = open("/home/js/code/JiraToken", "r")
    jira_token = file.readline()[:-1]  # remove the trailing newline character
    file.close()
    user = "jean-sacha.melon@smarkets.com"
    url = """https://notsmarkets.atlassian.net/"""
    return Jira(url=url, username=user, password=jira_token)


# this is for testing only
jira_instance = get_jira_instance()

# get information about ticket TFI-32
# json_jira = jira_instance.issue(key="TFI-32")
# pprint.pprint(json_jira)

# find out what fields exist
# fields = jira_instance.get_all_fields()

# get all the fields of issue TFI-32
# fields = jira_instance.issue_fields("TFI-32")
# pprint.pprint(fields)

# add an attachment to issue TFI-32
# jira_instance.add_attachment("TFI-32", "/home/js/Downloads/DSC_0588.JPG")

# This example shows that the create timestamp cannot be set when creating an issue via the API
# When removing the "created_at" field the call succeeds
# jira_instance.issue_create(
#     fields={
#         "project": {"key": "TFI"},
#         "issuetype": {"name": "Task"},
#         "summary": "created with python",
#         "description": "whatever suits you",
#         "created_at": "2020-05-26T19:14:03.557Z",
#     })


