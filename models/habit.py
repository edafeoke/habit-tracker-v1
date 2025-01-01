"""
Habit model
"""

class Habit:
    def __init__(self, id, name, description, start_date, end_date, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id