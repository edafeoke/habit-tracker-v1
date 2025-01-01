"""
User model
"""

from database import conn
from sqlite3 import IntegrityError
from rich import print

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        try:
            sql = "INSERT INTO users (username, password) VALUES (?, ?)"
            conn.execute(sql, (self.username, self.password))
            conn.commit()
            print(f"[green]User {self.username} created successfully![/green]")
        except IntegrityError:
            print(f"[red]Username already exist![/red]")
    
    def update(self, user_id, username, password):
        if not user_id:
            print("[red]User ID is required![/red]")
            return

        sql = "SELECT * FROM users WHERE id = ?"
        cursor = conn.execute(sql, (user_id,))
        user = cursor.fetchone()
        print(f"username: {username}")
        print(f"password: {password}")
        print("\n")
        print("The user to be updated is: ", user)
        print(f"ID: {user[0]}")
        print(f"Username: {user[1]}")
        print(f"Password: {user[2]}")
        
        if user is None:
            print(f"[red]User {user_id} not found![/red]")
            return

        if username != "":
            self.username = username
        else:
            self.username = user[1]

        if password != "":
            self.password = password
        else:
            self.password = user[2]

        self.id = user_id

        try:
            sql = "UPDATE users SET username = ?, password = ? WHERE id = ?"
            conn.execute(sql, (username, password, user_id))
            conn.commit()
            print(f"[green]User {username} updated successfully![/green]")
        except IntegrityError:
            print(f"[red]Username already exist![/red]")