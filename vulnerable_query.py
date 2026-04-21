def get_user_account(username, password):
    # Vulnerable SQL query construction (string concatenation)
    query = "SELECT * FROM Users WHERE username = '" + username + \
            "' AND password = '" + password + "'"

    # Simulated execution (unsafe practice)
    print(query)

    return query


# Example usage (simulating user input)
user_input = "' OR '1'='1"
password_input = "anything"

get_user_account(user_input, password_input)
