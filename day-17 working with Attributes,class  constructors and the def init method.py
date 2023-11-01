class user:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user_1 = user("456", "harshad")
user_2 = user("4556", "hars")
print(user_1.username)
print(user_1.id)
