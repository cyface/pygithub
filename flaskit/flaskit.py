"""testing flask framework"""
from pygithub3 import Github
from docutils import core
from flask import Flask, session, redirect, url_for, request, render_template, flash
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
        gh = Github(token=session.get('user_id'))
        username = gh.users.get().login
    else:
        gh = Github()
        username = None

    result = gh.gists.get(3156583)
    content = result.files.get('readme.rst').content
    parts = core.publish_parts(source=content, writer_name='html')
    body = parts.get('html_body')

    return render_template("base.html", body=body, title="Welcome", username=username)

@app.route('/login')
def login():
    if session.get('user_id', None) is None:
        return github.authorize()
    else:
        flash('You are already logged in')
        next_url = request.args.get('next') or url_for('index')
        return redirect(next_url)


@app.route('/oauth/callback')
@github.authorized_handler
def authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        return redirect(next_url)

    token = resp['access_token']

    session['user_id'] = token

    flash('You were successfully logged in')

    return redirect(next_url)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX v~XHH!jmN]LWX/,?RT'
    app.debug = True
    app.run()