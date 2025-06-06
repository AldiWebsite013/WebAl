from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import json
import os

app = Flask(__name__)
DATA_FILE = "timer_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"start_time": None, "end_time": None}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.route("/get_timer")
def get_timer():
    data = load_data()
    return jsonify(data)

@app.route("/start_timer", methods=["POST"])
def start_timer():
    now = datetime.utcnow()
    end_time = now + timedelta(seconds=50)  # Timer 50 detik
    data = {
        "start_time": now.isoformat(),
        "end_time": end_time.isoformat()
    }
    save_data(data)
    return jsonify({"status": "started", "end_time": data["end_time"]})

if __name__ == "__main__":
    app.run(debug=True)
