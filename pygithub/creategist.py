"""creates a github gist"""

from pygithub3 import Github

gh = Github(login='timlwhite', password='p1Decker')

gists = gh.gists.list().all()
print (gists)

gist_file = open('readme.rst', 'r')
file_contents = file.read()
file.close()
#result = gh.gists.create(dict(description='upload test', public=True, files={'upload.py': {'content': file_contents}}))

result = gh.gists.update(3156583, dict(description='desc', public=True, files={'readme.rst': {'content': file_contents}}))

print result

result = gh.gists.get(3156583)

#print (result.files.get('upload.py').content)
#print (result.files.get('data').content)
print (result.files.get('readme.rst').content)


gists = gh.gists.list().all()
print (gists)
