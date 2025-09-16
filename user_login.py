# user_login.py
"""
Feature: User Login System
Task ID: T-01
Description:
    This feature provides a simple user login simulation.
    - Accepts username and password.
    - Checks credentials against stored values.
    - Displays login success or failure.
"""

# Simulated user database
users = {
    "ratul": "password123",
    "rafid": "cocosub2025"
}

def login(username: str, password: str) -> bool:
    """
    Check if the provided username and password match.
    Returns True if login is successful, False otherwise.
    """
    if username in users and users[username] == password:
        return True
    return False


if __name__ == "__main__":
    print("=== User Login Simulation ===")
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if login(user, pwd):
        print(f"✅ Login successful! Welcome, {user}.")
    else:
        print("❌ Login failed. Invalid username or password.")
