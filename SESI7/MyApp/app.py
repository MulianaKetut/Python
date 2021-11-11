from flask import Flask, request, render_template, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Index Page</h1>'


# @app.route('/hello')
# def hello():
#     a = 10
#     return f"hello {a}"


# @app.route('/<name>')
# def hello_name(name):
#     '''escape digunakan untuk menjaga dari serangan injection'''
#     return f"Hello, {escape(name)}"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do_the_login()'
    else:
        return 'show_the_login_form()'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.run(debug=True)
