from flask import Flask, render_template, request, make_response
app = Flask(__name__)

# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'POST' and \
#         request.form['username'] == 'admin':
#         return redirect(url_for('success'))
#     return redirect(url_for('index'))


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug = True)
    