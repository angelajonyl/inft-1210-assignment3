import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Reyes ECS Container!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # default to 8080
    app.run(host='0.0.0.0', port=port)
