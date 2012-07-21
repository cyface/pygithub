"""Creates a Github Repo"""

from pygithub3 import Github

gh = Github(login='timlwhite', password='p1Decker')

repo_data = {
    "name": "Mechanical-Repo",
    "description": "This is my first repo",
    "homepage": "https://github.com",
    "private": False,
    "has_issues": False,
    "has_wiki": False,
    "has_downloads": False
}

gh.repos.create(data=repo_data)

timlwhite_repos = gh.repos.list().all()
print (timlwhite_repos)