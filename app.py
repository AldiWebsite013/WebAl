from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import json, os

app = Flask(__name__)
DATA_FILE = "timer_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"end_time": None}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.route("/get_timer")
def get_timer():
    data = load_data()
    return jsonify(data)

@app.route("/set_timer", methods=["POST"])
def set_timer():
    time_str = request.args.get("time", "")
    try:
        h, m, s = map(int, time_str.split(":"))
        delta = timedelta(hours=h, minutes=m, seconds=s)
        end_time = datetime.utcnow() + delta
        save_data({"end_time": end_time.isoformat()})
        return jsonify({"status": "ok", "end_time": end_time.isoformat()})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
