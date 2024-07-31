def get_user_data(username):
    # Dummy user data
    users = {
        "john": {"name": "John Doe", "age": 30, "city": "New York"},
        "jane": {"name": "Jane Smith", "age": 25, "city": "Los Angeles"},
    }
    return users.get(username.lower())

if __name__ == "__main__":
    print(get_user_data("john"))
