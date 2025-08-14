# api.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simple in-memory store (reset when server restarts)
points = 0

@app.route('/get_points', methods=['GET'])
def get_points():
    return jsonify({"points": points})

@app.route('/add_point', methods=['POST'])
def add_point():
    global points
    points += 1
    return jsonify({"points": points})  # must return valid JSON


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
