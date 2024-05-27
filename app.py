from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Por favor Humberto não nos deixe de DP"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
