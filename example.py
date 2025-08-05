class UserProfile:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def show_profile(self):
        print("User Profile")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)

user1 = UserProfile("Alice", 25, "alice@example.com")
user1.show_profile()

user2 = UserProfile("Bob", 30, "bob@example.com")
user2.show_profile()
