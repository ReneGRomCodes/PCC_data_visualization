import unittest
import python_repos


class ReposTestCase(unittest.TestCase):
    """Tests for 'python_repos.py'."""

    def test_status_code(self):
        """Does the API call return 'Status code: 200'."""
        r, response_dict = python_repos.api_call()
        self.assertEqual(r.status_code, 200)

    def test_len_names(self):
        """Test if the number of returned repositories is 30."""
        r, response_dict = python_repos.api_call()
        names, plot_dicts = python_repos.repo_explore(response_dict)
        self.assertEqual(len(names), 30)


if __name__ == "__main__":
    unittest.main()
