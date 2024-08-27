class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.credits = 15
        self.books = []

class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password)
        return True

    def authenticate(self, username, password):
        if username in self.users and self.users[username].password == password:
            return True
        return False

    def get_user_books(self, username):
        if username in self.users:
            return self.users[username].books
        return []

    def purchase_book(self, username, book):
        if username in self.users:
            user = self.users[username]
            if user.credits >= book.price:
                user.credits -= book.price
                user.books.append(book)
                return True
        return False