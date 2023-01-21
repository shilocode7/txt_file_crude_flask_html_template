from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def read_file():
    try:
        with open('sample.txt', 'r') as f:
            contents = f.read()
        return jsonify(contents)
    except Exception as e:
        return jsonify(str(e)), 500
    


@app.route('/add', methods=['POST'])
def add_to_file():
    try:
        text = request.json.get('text')
        with open('sample.txt', 'a') as f:
            f.write(text)
        return jsonify("Text added successfully.")
    except Exception as e:
        return jsonify(str(e)), 500
    
@app.route('/edit', methods=['PUT'])
def edit_file():
    try:
        text = request.json.get('text')
        with open('sample.txt', 'w') as f:
            f.write(text)
        return jsonify("File edited successfully.")
    except Exception as e:
        return jsonify(str(e)), 500
    
########## serch tests############
    #####serch how many times a word is in a text
@app.route('/search/<word>', methods=['GET', 'GET'])
def search_word(word):
    try:
        with open('sample.txt', 'r') as f:
            contents = f.read().lower()
            count = contents.count(word)
            return jsonify(count)
    except Exception as e:
        return jsonify(str(e)), 500
######## End serch how many times a word is in a text 

#### serch word####



###End serch word ###

if __name__ == '__main__':
    app.run(debug=True)
