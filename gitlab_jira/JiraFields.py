class JiraFields:
    def __init__(self):
        self.fields = {}

    def populate_from_gitlab_issue_json(self, gitlab_issue_json):
        self.fields = {"summary": gitlab_issue_json["title"],
                       "description": gitlab_issue_json["description"],
                       }

    def add_title(self, title):
        self.fields["title"] = title

