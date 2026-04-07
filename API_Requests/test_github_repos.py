import unittest
import requests

class TestGitHubRepos(unittest.TestCase):
    def test_get_repos(self):
        url = 'https://api.github.com/search/repositories'
        params = {'q': 'language:python', 'sort': 'stars', 'order': 'desc'}
        r = requests.get(url, params=params)
        status_code = r.status_code

        if status_code != 200:
            self.fail(f"API request failed with status code {status_code}")
        
        self.assertTrue(True)
        
    def test_language_repos(self):
        url = 'https://api.github.com/search/repositories'
        params = {'q': 'language:python', 'sort': 'stars', 'order': 'desc'}
        r = requests.get(url, params=params)
        response_dict = r.json()
        repo_dicts = response_dict.get('items', [])
        
        if not repo_dicts:
            self.fail("No repositories found for this language.")
        
        self.assertTrue(len(repo_dicts) > 0)


if __name__ == '__main__':
    unittest.main() 