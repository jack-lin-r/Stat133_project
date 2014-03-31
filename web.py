import flask, flask.views
import json

# extra1
from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = flask.Flask(__name__)
app.secret_key = "starcraft"

class Main(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')

    def post(self):

        return flask.request.form['expression']
'''
class About(flask.views.MethodView):
    def get(self):
        return flask.render_template('about.html')
'''
class Contact(flask.views.MethodView):
    def get(self):
        return flask.render_template('contact.html')

class Lion(flask.views.MethodView):
    def get(self):
        return flask.render_template('test.html')

app.add_url_rule('/',
    view_func=Main.as_view('index'),
    methods=['GET','POST'])
'''
app.add_url_rule('/about',
    view_func=About.as_view('about'),
    methods=['GET'])
'''
app.add_url_rule('/contact',
    view_func=Contact.as_view('contact'),
    methods=['GET'])

app.add_url_rule('/lion',
    view_func=Lion.as_view('lion'),
    methods=['GET'])

# extra 2
@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        flash('Example of Flashing)
        flash('Example of Flashing 2')
        return render_template('about.html')


app.debug = True
app.run()

