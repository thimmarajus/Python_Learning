from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<int:score>/')
#def hello(score):
def hello_name(score):
  return render_template('hello_03.html', marks = score)

# return "<html><body><h1>"Hello World"</h1></body></html>"
  #return render_template('hello.html')
#def hello_name(user):
#def hello_name(user):
# return render_template('hello_02.html', name = user)

if __name__ == '__main__':
  app.run()
#import sqlite3

#conn = sqlite3.connect('database.db')
#print "opened database sucessfully";
