import pytest
import requests
import json


class TestAPI:
    token = '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'
    headers = {"Authorization": f'token {token}'}

    @pytest.mark.api
    def test_github_user(self):
        end_point = 'https://api.github.com/user'
        user = requests.get(url=end_point, headers=self.headers)
        user_data = json.loads(user.content)
        assert user_data.get("login") == "neri321"

    @pytest.mark.skip
    def test_delete_repo(self):
        end_point = 'https://api.github.com/repos/neri321/api_test_repo'
        response = requests.delete(url=end_point, headers=self.headers)
        pass

    @pytest.mark.api
    def test_update_repo(self):
        end_point = 'https://api.github.com/repos/neri321/api_test_repo_1'
        repo_data = {'name': 'api_test_repo_one',
                     'description': 'my api_test_repo',
                     'private': False}
        response = requests.patch(url=end_point, headers=self.headers, json=repo_data)
        new_repo_name = response.json().get('html_url')
        assert new_repo_name.endswith(repo_data.get('name'))

    @pytest.mark.api
    def test_github_create_repo(self):
        end_point = 'https://api.github.com/user/repos'
        repo_data = {'name': 'Final_project_AUT_G9_Moroz_Iryna',
                     'description': 'my api_test_repo',
                     'private': False}
        response = requests.post(url=end_point, headers=self.headers, json=repo_data)
        new_repo_name = response.json().get('html_url')
        assert new_repo_name.endswith(repo_data.get('name'))
