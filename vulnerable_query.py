from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def get_user():
    username = request.args.get("username")

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE users (username TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin')")

    # Vulnerable SQL injection (REALISTIC PATTERN)
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    return str(cursor.fetchall())


if __name__ == "__main__":
    app.run()
