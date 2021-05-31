from flask import Flask,jsonify
import requests
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

@app.route('/')
def get():
    return "WELCOME TO THE COURSE API"

@app.route('/users',methods=['GET'])
def getUsers():
  users = requests.get('https://jsonplaceholder.typicode.com/users')
  return jsonify(users.json())

@app.route('/users/<int:userId>/albums',methods=['GET'])
def get_al(userId):
  x= requests.get('https://jsonplaceholder.typicode.com/albums')
  albums=x.json()
  filtered_albums = list(filter(lambda album: album.get("userId") == userId, albums))
  return jsonify(filtered_albums)



if __name__=="__main__":
    app.run(debug=True)