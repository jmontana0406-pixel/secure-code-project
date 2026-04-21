import sqlite3

def get_user_account(username):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Simulated unsafe SQL injection vulnerability
    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor.execute(query)  # <-- THIS is what Sonar detects
    return cursor.fetchall()


# Simulated malicious input
user_input = "' OR '1'='1"

get_user_account(user_input)
