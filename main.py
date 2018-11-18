from flask import Flask, render_template, request
app = Flask(__name__)

ntp = __import__('DataScience')

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
    if request.method=='POST':
        text = request.form['text']
        word_type = ntp.stop_words(ntp.word_tokenize(text))
        return render_template("results.html",
        text = text,
        useful = word_type[0],
        stop = word_type[1],
        punctuation = word_type[2],
        stemlem = ntp.stemlem(ntp.word_tokenize(text)),
        pos = ntp.pos_tagging(ntp.word_tokenize(text)),
        gram = ntp.grams(ntp.word_tokenize(text)),
        freqstats=ntp.frequency_statistics(text))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
