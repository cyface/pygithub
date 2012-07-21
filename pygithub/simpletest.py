"""Simple Test of PyGithub"""

from pygithub3 import Github

gh = Github(login='timlwhite', password='p1Decker')

timlwhite = gh.users.get()
print (timlwhite)

timlwhite_repos = gh.repos.list().all()
print (timlwhite_repos)

myrepo = gh.repos.get(user="timlwhite", repo="Mechanical-Repo")
print (myrepo)

timlwhite_watches = gh.repos.watchers.list_repos().all()
print (timlwhite_watches)

