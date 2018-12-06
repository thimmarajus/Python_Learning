"""from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
 return "Hello World"

if __name__ == "__main__":
 app.run()"""
"""from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return 'Hello World from Python Flask!'

@app.route("/hello")
def hello():
    return "Hello World"

#@app.route("/add")
#def add():
#    print(5 + 10)

@app.route("/members/<string:name>/")
def getMember(name):
    return name

if __name__ == "__main__":
   app.run()
