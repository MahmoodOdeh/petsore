import os
from dotenv import load_dotenv
from jira import JIRA

from infra.config_handler import ConfigHandler


class JiraClient:
    def __init__(self):
        load_dotenv()
        config_file_path = r'C:\Users\odehm\Desktop\repos\petsore\config.json'
        self.config_handler = ConfigHandler(config_file_path)
        self.jira_url = self.config_handler.get_config_value('jira_url')
        self.TOKEN = os.getenv("JIRA_TOKEN")
        self.jira_user = self.config_handler.get_config_value('jira_user')
        self.auth_jira = JIRA(basic_auth=(self.jira_user, self.TOKEN), options={'server': self.jira_url})

    def create_issue(self, summary, description, project_key, issue_type='Bug'):
        print("summary", summary)
        print("description", description)
        print("project_key", project_key)
        print("issue_type", issue_type)

        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }
        new_issue = self.auth_jira.create_issue(fields=issue_dict)
        return new_issue.key
