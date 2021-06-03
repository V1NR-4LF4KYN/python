class User:
    user_count = 0
    
    def __init__(self, username):
        self.username = username
        User.user_count += 1
        

u1 = User("hhheee")
print(u1.user_count)

u2 = User("hegweg")
print(u1.user_count)