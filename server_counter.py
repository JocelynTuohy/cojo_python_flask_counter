from flask import Flask, render_template, redirect, session
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

@app.route('/countTwo', methods=['POST'])
def counter():
    session['count'] += 1
    return redirect('/')

app.run(debug=True)
