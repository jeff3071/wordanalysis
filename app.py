import flask
from flask import render_template
from flask import request
from model.analysis import main

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/res', methods=['GET'])
def getdata():
    return render_template('index.html')

@app.route('/res', methods=['POST'])
def submit():
    article1 = request.form.get('article1')
    article2 = request.form.get('article2')
    return main(article1, article2)


if __name__ == '__main__':
    app.run()