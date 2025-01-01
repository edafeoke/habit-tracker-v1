"""
Habit Tracker v1 entry point
"""

from controllers.user_controllers import create_user, update_user, delete_user, all_users
from pwinput import pwinput
from rich import print

def run():
    while True:
        command = input("(hbttracker)> ")
        if command == "exit":
            break
        elif command == "create user":
            username = input("Username: ")
            password = pwinput("Password: ")
            create_user(username, password)
        elif command == "update user":
            user_id = input("User ID: ")
            username = input("Username: ")
            password = pwinput("Password: ")
            update_user(user_id, username, password)
        else:
            print("\n[yellow]Command not found[/yellow]")

    print("Goodbye!")

if __name__ == "__main__":
    run()
    from database import conn
    conn.close()