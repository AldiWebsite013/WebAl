from flask import Flask, render_template
import sqlite3
import time

app = Flask(__name__)

@app.route("/timer/<int:user_id>")
def countdown(user_id):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT duration, start_time FROM countdown WHERE user_id = ? ORDER BY start_time DESC LIMIT 1", (user_id,))
    row = cur.fetchone()
    conn.close()

    if not row:
        return "⛔ Timer tidak ditemukan."

    duration, start_time = row
    remaining = duration - (int(time.time()) - start_time)
    if remaining < 0:
        remaining = 0

    return render_template("countdown.html", seconds=remaining)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
