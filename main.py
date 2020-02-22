import sys
sys.path.insert(1, './Database')
import database as dbLib# = __import__('./Database/database.py')
db = dbLib.Database()

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

'''
# Naming and variables
@app.route('/name/<name>/<int:score>')
def hello(name,score):
    return render_template('name.html', name=name, marks=score)
'''

@app.route('/results',methods=['POST', 'GET']) 
def result():
    #text = request.form['text']#For POST
    search = request.args.get("search")
    examples = db.search(search)
    return render_template("results.html",search=search,len=len,examples=examples)

@app.route('/example/<int:exampleId>',methods=['POST', 'GET']) 
def example(exampleId):
    #exampleId = int(request.args.get("id"))
    example = db.getID(exampleId)
    return render_template("example.html",example=example)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
