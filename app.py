from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Basic REST API!'

@app.route('/status')
def status():
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(port=3333)