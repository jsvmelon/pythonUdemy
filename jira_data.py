from atlassian import Jira
import pprint


def get_jira_instance():
    """
    Constructs an instance of the Atlassian Jira object to easily access Jira
    via the API.
    :return: instance of the Atlassian Jira object
    """
    # file = open("/home/js/code/JiraToken", "r")
    file = open("/home/js/code/Smarkets_Jira_token", "r")
    jira_token = file.readline()[:-1]  # remove the trailing newline character
    file.close()
    user = "jean-sacha.melon@smarkets.com"
    # url = """https://notsmarkets.atlassian.net/"""
    url = """https://smarkets-jira.atlassian.net/"""
    return Jira(url=url, username=user, password=jira_token)


def escape_for_jira(text: str):
    res = text.replace('"', r'\"')
    res = res.replace('[', r'\\[')
    res = res.replace(']', r'\\]')
    return res


def find_entries_leg_core():  # TODO
    """
    Finds ticket from legacy in core
    :return: None
    """
    jira_instance = get_jira_instance()

    number_of_issues = jira_instance.get_project_issues_count(project="LEG")
    start_position = 0
    page_size = 100
    keys_core = []
    while start_position < number_of_issues:
        print("loading from position {}".format(start_position))
        tickets = jira_instance.get_all_project_issues("LEG", limit=page_size, start=start_position)
        for ticket in tickets:
            summary_escaped = escape_for_jira(ticket["fields"]["summary"])
            jql_string = 'project = CORE AND summary ~ "{}"'.format(summary_escaped)
            data = jira_instance.jql(jql_string)
            found_number = data["total"]
            for i in range(0, found_number):
                keys_core.append(data["issues"][i]["key"])
                print(data["issues"][i]["key"])
        start_position += page_size


def find_duplicates_in_core():
    jira_instance = get_jira_instance()

    number_of_issues = jira_instance.get_project_issues_count(project="CORE")
    start_position = 0
    page_size = 100
    all_ticket_names = []
    ticket_keys = []  # corresponds to the names in all_ticket_names
    duplicate_keys = []
    duplicate_items_link = {}
    while start_position < number_of_issues:
        print("loading from position {}".format(start_position))
        print("number of duplicates {}".format(len(duplicate_keys)))
        res = jira_instance.get_all_project_issues("CORE", limit=page_size, start=start_position)
        for ticket in res:
            summary = ticket["fields"]["summary"]
            if summary in all_ticket_names:
                key = ticket["key"]
                duplicate_keys.append(key)
                position = all_ticket_names.index(summary)
                duplicate_items_link[key] = ticket_keys[position]

                # add an identifying comment to the issue
                jira_instance.issue_add_comment(
                    key,
                    "Duplicate of {} \nkrEtxm4ThHMW2b8QKTG4_target".format(ticket_keys[position])
                )
                jira_instance.issue_add_comment(
                    ticket_keys[position],
                    "Has duplicate {} \nkrEtxm4ThHMW2b8QKTG4_source".format(key)
                )
                print("duplicates mentioned in {} and {}".format(ticket_keys[position], key))
            else:
                all_ticket_names.append(ticket["fields"]["summary"])
                ticket_keys.append(ticket["key"])
        start_position += page_size
    print(duplicate_keys)


def create_empty_description() -> dict:
    return {
        "version": 1,
        "type": "doc",
        "content": []
    }


def insert_link(description: dict, text: str, address: str) -> dict:
    description["content"].append(
        {
            "type": "paragraph",
            "content": [
                {
                    "type": "text",
                    "text": text,
                    "marks": [
                        {
                            "type": "link",
                            "attrs": {
                                "href": address
                            }
                        }
                    ]
                }
            ]
        }
    )
    return description


jira_instance = get_jira_instance()
codeblock = r"""
{code}
find_api_resource(#smak_ctx{scope = Scope} = Ctx, Split) ->
    Type = to_atom(hd(Split), true),
    case lists:member(Type, [exchange_rates, contract_groups,
                             accounts, stats, sync, control]) of
        true ->
            TypeStr = atom_to_list(Type),
            Prefix = scope_prefix(Scope),
            SplitPath = convert(tl(Split)),
            io:fwrite("~p~n", [SplitPath]),
            smak_request:resource(Ctx#smak_ctx{split_path = SplitPath},
                                  list_to_atom("rest_" ++ TypeStr),
                                  Prefix ++ "/" ++ hd(Split) ++ "/");
        false ->
            smak_rsp:context_error(Ctx, not_found, [])
    end.
{code}
"""
# description = insert_link(create_empty_description(), "link", "http://google.com")
description = {
    "type": "codeBlock",
    "attrs": {
        "language": "javascript"
    },
    "content": [
        {
            "type": "text",
            "text": r"var foo = {};\nvar bar = [];"
        }
    ]
}
fields = {
    "project": {"key": "TRASH"},
    "issuetype": {"name": "Story"},
    "summary": "code block test",
    "description": description,
    "components": [{"name": "duplicate"}],
}
pprint.pprint(fields)
jira_instance.issue_create(fields)

jira_instance.issue_add_comment("SMK-8806", r"Some text before" +
                                codeblock +
                                r"some after")

jira_instance.issue_edit_comment("SMK-8806", "26331", codeblock)

# fields = {'description': 'This is a new description with a link:\n [Test|https://git.corp.smarkets.com/smarkets/smarkets/-/issues/13506]'}
# jira_instance.issue_update("CORE-22", fields)

# jira_instance.issue_add_comment(
#     "CORE-22",
#     "Some text before... [Test|https://git.corp.smarkets.com/smarkets/smarkets/-/issues/13506] Some afterwards")
#
# jsvmelon = "5e70c173b2e0f80c43c71475"
# smelon = "603822e28ff09800717a5f8c"

# jira_instance.user_deactivate(username="Jean-Sacha Melon")

# jira_instance.user_disable(userid)

# get information about ticket TFI-32
# json_jira = jira_instance.issue(key="MT-37")
# pprint.pprint(json_jira)
# print(len(json_jira["fields"]["comment"]["comments"]))

# jira_instance.issue_edit_comment("MT-37", "10081", "overwrite")

# find out what fields exist
# fields = jira_instance.get_all_fields()

# get all the fields of issue TFI-32
# fields = jira_instance.issue_fields("TFI-32")
# pprint.pprint(fields)

# add an attachment to issue MT-37
# jira_instance.add_attachment("MT-37", "/home/js/Downloads/1200px-React-icon.svg.png")

# add a comment with a reference to an attachment
# jira_instance.issue_add_comment("MT-37", "before picture of paint\n\n!1200px-React-icon.svg.png|width=275,height=183!\n\nafter picture of paint")

# jira_instance.issue_add_comment("MT-37", "before picture of paint\n\n!paint.jpeg|width=275,height=183!\n\nafter picture of paint")
# jira_instance.issue_add_comment("MT-37", "before picture of paint\n\n!Screenshot_from_2021-06-02_16-22-14.png|width=275,height=183!\n\nafter picture of paint")

# add something to the description with a reference to an attachment
# jira_instance.issue_update("MT-37", {'description': 'description before image\n\n!paint.jpeg|width=275,height=183!\n\ndescription after image'})

# jira_instance.update_issue_field("MT-37", {'summary': 'Jira migration test issue (modified)'})
# jira_instance.edit_issue("MT-37")

# jira_instance.update_issue_field("MT-37",
#                                  {'comment': {'comments': [
#                                      {'author': {'accountId': '70121:e2a35cca-3db6-4e76-9dfa-7f744ea4cfe8',
#                                                  'accountType': 'atlassian',
#                                                  'active': True,
#                                                  'avatarUrls': {
#                                                      '16x16': 'https://secure.gravatar.com/avatar/ff32b4121f95c17ba1aaf9b2ccaf3756?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNR-0.png',
#                                                      '24x24': 'https://secure.gravatar.com/avatar/ff32b4121f95c17ba1aaf9b2ccaf3756?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNR-0.png',
#                                                      '32x32': 'https://secure.gravatar.com/avatar/ff32b4121f95c17ba1aaf9b2ccaf3756?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNR-0.png',
#                                                      '48x48': 'https://secure.gravatar.com/avatar/ff32b4121f95c17ba1aaf9b2ccaf3756?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNR-0.png'},
#                                                  'displayName': 'Nithya '
#                                                                 'Rajashekhar',
#                                                  'self': 'https://notsmarkets.atlassian.net/rest/api/2/user?accountId=70121%3Ae2a35cca-3db6-4e76-9dfa-7f744ea4cfe8',
#                                                  'timeZone': 'Europe/London'},
#                                       'body': 'Author: Nithya Rajashekhar '
#                                               '2021-06-09T15:37:25.004Z\n'
#                                               '[Attachment '
#                                               'Screenshot_from_2021-06-02_16-22-14 '
#                                               '|https://git.corp.smarkets.com/smarkets/smarkets/uploads/7144a7db262d323adc1db74725fd2ae5/Screenshot_from_2021-06-02_16-22-14.png]random '
#                                               'image to test image creation on '
#                                               'jira',
#                                       'created': '2021-06-09T17:29:53.593+0100',
#                                       'id': '10076',
#                                       'jsdPublic': True,
#                                       'self': 'https://notsmarkets.atlassian.net/rest/api/2/issue/10114/comment/10076',
#                                       'updateAuthor': {'accountId': '70121:e2a35cca-3db6-4e76-9dfa-7f744ea4cfe8',
#                                                        'accountType': 'atlassian',
#                                                        'active': True,
#                                                        'avatarUrls': {
#                                                            '16x16': 'https://secure.gravatar.com/avatar/ff32b4121f95c17ba1aaf9b2ccaf3756?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNR-0.png',
#                                                            '24x24': 'https://secure.gravatar.com/avatar/ff32b4121f95c17ba1aaf9b2ccaf3756?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNR-0.png',
#                                                            '32x32': 'https://secure.gravatar.com/avatar/ff32b4121f95c17ba1aaf9b2ccaf3756?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNR-0.png',
#                                                            '48x48': 'https://secure.gravatar.com/avatar/ff32b4121f95c17ba1aaf9b2ccaf3756?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNR-0.png'},
#                                                        'displayName': 'Nithya '
#                                                                       'Rajashekhar',
#                                                        'self': 'https://notsmarkets.atlassian.net/rest/api/2/user?accountId=70121%3Ae2a35cca-3db6-4e76-9dfa-7f744ea4cfe8',
#                                                        'timeZone': 'Europe/London'},
#                                       'updated': '2021-06-09T17:29:53.593+0100'}]}})
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
