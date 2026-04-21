import sqlite3

def get_user(username):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE users (username TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin')")

    # 🚨 Vulnerable SQL injection pattern
    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor.execute(query)  # <-- critical sink
    results = cursor.fetchall()

    return results


# Simulated malicious input
user_input = "' OR '1'='1"
print(get_user(user_input))
