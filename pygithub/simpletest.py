"""Simple Test of PyGithub"""

from pygithub3 import Github
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('pygithub.cfg')

username = config.get("github", "username")
password = config.get("github", "password")

gh = Github(login=username, password=password)

timlwhite = gh.users.get()
print (timlwhite)

timlwhite_repos = gh.repos.list().all()
print (timlwhite_repos)

myrepo = gh.repos.get(user="timlwhite", repo="Mechanical-Repo")
print (myrepo)

timlwhite_watches = gh.repos.watchers.list_repos().all()
print (timlwhite_watches)