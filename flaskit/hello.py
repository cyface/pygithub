"""testing flask framework"""
from pygithub3 import Github
from docutils import core
from flask import Flask, session, redirect, url_for, request
from flask.ext.github import GithubAuth

app = Flask(__name__)

github = GithubAuth(
    client_id='b13a4ddc0b9c94b27d82',
    client_secret='9930844b8fafcbd10c37632dd576ee8d8014030a',
    session_key='user_id'
)

@app.route('/')
def index():
    if 'user_id' in session:
        return session.get('user_id')

    gh = Github()
    result = gh.gists.get(3156583)

    content = result.files.get('readme.rst').content

    html = core.publish_string(source=content, writer_name='html')

    return html

@app.route('/login')
def login():
    if session.get('user_id', None) is None:
        return github.authorize()
    else:
        return 'Already logged in'


@app.route('/oauth/callback')
@github.authorized_handler
def authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        return redirect(next_url)

    token = resp['access_token']

    session['user_id'] = token

    return 'Success'

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX v~XHH!jmN]LWX/,?RT'
    app.debug = True
    app.run()