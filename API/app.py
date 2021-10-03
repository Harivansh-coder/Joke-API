from flask import Flask, jsonify
import data


app = Flask(__name__)

jokes = data.joke

@app.route('/')
def index():
    return "Joke API"

@app.route("/jokes",methods = ['GET'])
def get():
    return jsonify({'jokes':jokes})

if __name__ == "__main__":

    app.run(debug=True)

  



