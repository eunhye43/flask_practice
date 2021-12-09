from flask import Flask, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'get some sleep'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
        "<b><a href = '/logout'>click here to log out </a></b>"

    return "you are not logged in <br><a href = '/loging'></b>" + \
        "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        print("---------------------")
        print(request.form['username'])
        print("---------------------")
        return redirect(url_for('index'))
    return '''

    <form action = "" method = "post">
        <p><input type = text name = username></p>
        <p><input type = submit value = Login></p>
    </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)
    