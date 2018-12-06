#from flask import Flask, flash, redirect, render_template, request, session, abort

#app = Flask(__name__)

#@app.route("/")
#def index():
#    return "Flask App!"

#@app.route("/")
#def hello(name):
#    return render_template(
#        'test.html',name=name)

#if __name__ == "__main__":
#   app.run()
"""from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Index!"
 
@app.route("/hello/")
def hello():
    return "Hello World!"
 
@app.route("/members")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return name
 
if __name__ == "__main__":
    app.run()"""
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
 return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
       return redirect(url_for('hello_admin'))
    else:
       return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)

#@app.route('/guest/<guest>')
