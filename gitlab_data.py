import requests
import json

GITLAB_ISSUE_BASE_URL = "https://git.corp.smarkets.com/api/v4/projects/98/issues"
file = open("/home/js/code/GitLabToken", "r")
GL_TOKEN = file.readline()[:-1]  # remove the trailing newline character


def get_gitlab_data_page(base_path: str, page: int, gl_token: str):
    """
    Get an issue page from GitLab for project 98. Start with page 1 and check
    the next_page return to check if there is another page.
    :param gl_token: the gitlab token
    :param base_path: the url base path defining what data type is read
    :type page: int page number
    :raises ValueError: when page is smaller than 1
    :param page: integer specifying the issue page to be requested
    :return: A tuple of (current_page, total_pages, content_json)
    """
    if page < 1:
        raise ValueError

    ITEMS_PER_PAGE = "5"  # 100 is the maximum
    url = base_path + "?per_page=" + ITEMS_PER_PAGE + "&page=" + str(page)

    response = requests.get(url=url, headers={"Private-Token": gl_token})
    content_json: list = json.loads(response.text)

    total_pages: int = int(response.headers["X-Total-Pages"])
    return (total_pages, content_json)


current_page = 1
total_pages, issues_json_page = get_gitlab_data_page(GITLAB_ISSUE_BASE_URL, current_page, GL_TOKEN)
issues_json = issues_json_page

while current_page < total_pages:
    # get all the notes for each issue
    # for issue in issues_json_page:
    #     note_url = issue["_links"]["notes"]
    #     get_gitlab_data_page(note_url, 1, GL_TOKEN)
    current_page += 1
    total_pages, issues_json_page = get_gitlab_data_page(GITLAB_ISSUE_BASE_URL, current_page, GL_TOKEN)
    issues_json.extend(issues_json_page)

# GET /projects/:id/issues/:issue_iid/related_merge_requests
# GET /projects/:id/issues/:issue_iid/resource_state_events
# GET /projects/:id/issues/:issue_iid/links
