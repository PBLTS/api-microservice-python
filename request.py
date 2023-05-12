from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route('/tipo')
def home():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    return response.json()


if __name__ == '__main__':
    app.run()
