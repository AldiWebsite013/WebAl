import sqlite3
conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS countdown (
    user_id INTEGER,
    duration INTEGER,
    start_time INTEGER
)
""")
conn.commit()
conn.close()
