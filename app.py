import os
import random
import json
from flask import Flask, render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from models import db
from dotenv import load_dotenv
load_dotenv('.env')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        id = random.randint(0, 10000000)
        return redirect(url_for("form", id = id))
    return render_template('index.html')
 
@app.route('/form/<int:id>', methods=['GET', 'POST'])
def form(id):
    if request.method == 'POST':
        print(request.form)
    with open('form.json') as test_file:
        form = json.load(test_file)
    parts = ['part1.html', 'part2.html', 'part3.html', 'part4.html', 'part5.html', 'part6.html', 'part7.html', 'part8.html', 'part9.html']
    parts = ['form_parts/' + x for x in parts]
    return render_template('form.html', form=parts)
 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)