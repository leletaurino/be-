from flask import Flask, request, render_template, redirect, make_response, jsonify
from markupsafe import escape
from flask import url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from datetime import datetime, timedelta

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'fwefew32323432wfwgferge!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rootadmin@localhost/testdb'

# manager = Manager(app)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now().date(), nullable=False)
    expiration_on = db.Column(db.DateTime(), default=datetime.now().date() + timedelta(days=30), nullable=False)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)


db.create_all()
db.session.commit()

CORS(app)


@app.errorhandler(404)
def page_not_found(error):
    print('error: ', error)
    return render_template('page_not_found.html', error=error), 404


@app.route('/home')
def home():
    return """
    <h1>Home</h1>
        <br>
        
    <a href="/user/ant">go to Username</a>
        <br>

    <a href="/post/1">go to Post</a>
        <br>

    <a href="/path/subpath">go to Subpath</a>
    """


def do_the_login(error):
    return render_template('login.html', error=error)


def valid_login(username, password):
    print('credentials: \n', username, password, sep='\t')
    if username and password:
        return True
    else:
        return False


@app.route('/check_data', methods=['POST'])
def check_user_data():
    print('sent args: ', request.json)
    return {"resp": "ok"}


@app.route('/', methods=['GET', 'POST'])
def login_without_name():
    error = None

    if request.method == 'GET':
        print('get args: ', request.args.to_dict())
        return do_the_login(error)
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return redirect(url_for('home'))  # log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
            return do_the_login(error)


@app.route('/user/<string:username>', methods=['GET', 'POST'])
def show_user_profile(username):
    user = {
        'username': username,
        'theme': render_template('helloworld.html'),
        'image': 'https://cdn.gelestatic.it/deejay/sites/2/2016/02/castelluccio.jpg'
    }
    # show the user profile for that user
    resp = make_response(f'ciao {escape(username)}')

    # user['resp'] = resp
    print(resp.get_data().decode('utf-8'))
    resp.headers['X-Something'] = 'A value'
    return user


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'The Subpath is: {escape(subpath)}'


with app.test_request_context():
    print(url_for('home'))
    # print(url_for('login'))
    # print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='John Doe'))

if __name__ == "__main__":
    # [START trace_demo_create_exporter]
    # createMiddleWare(StackdriverExporter())
    # [END trace_demo_create_exporter]

    # debug_toggle = False if os.environ.get("FLASK_ENV", '') != 'development' else True
    debug_toggle = True
    app.run(debug=debug_toggle, host='127.0.0.1', port=8080)
