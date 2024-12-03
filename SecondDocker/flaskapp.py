from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Lukesh Kumar Kalam's Flask application "

# API route to get data
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "Hello, World!",
        "status": "success"
    }
    return jsonify(data)

# API route to post data
@app.route('/api/data', methods=['POST'])
def post_data():
    incoming_data = request.json
    response = {
        "received": incoming_data,
        "status": "success"
    }
    return jsonify(response), 201

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

