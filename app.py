from flask import Flask, request, jsonify
from user_data import get_user_data

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is the friendly AI chatbot!"

@app.route('/user/<username>', methods=['GET'])
def user(username):
    user_info = get_user_data(username)
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
