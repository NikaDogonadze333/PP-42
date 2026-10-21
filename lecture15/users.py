class User:
    status = "Active"

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def get_info(self):
        print(f"მომხმარებელი: {self.username} | ელ-ფოსტა: {self.email} | ასაკი: {self.age} | სტატუსი: {User.status}")

user1 = User("nikolozi", "noko@gmail.com", 19)
user2 = User("mariami", "mari@gmail.com", 20)

user1.get_info()
user2.get_info()

print(f"User1 სტატუსი: {user1.status}")
print(f"User2 სტატუსი: {user2.status}")