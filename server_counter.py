from flask import Flask, render_template, session
# import re

app = Flask(__name__)
app.secret_key = 'SecretCounterKeyWoot'



@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('index.html')

# @app.route('/counter')
# def counter():
#     session['count']
#     return redirect('/')

app.run(debug=True)
