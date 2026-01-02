from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def users():
    return jsonify([
        {"id": 1, "name": "Alice", "role": "admin"},
        {"id": 2, "name": "Bob", "role": "user"}
    ])

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
