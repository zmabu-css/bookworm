class Book:
    def __init__(self, id, title, author, description, price, thumbnail):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.price = price
        self.thumbnail = thumbnail

class BookDatabase:
    def __init__(self):
        self.books = [
            Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "A novel about the American Dream", 10.99, "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/The_Great_Gatsby_Cover_1925_Retouched.jpg/330px-The_Great_Gatsby_Cover_1925_Retouched.jpg"),
            Book(2, "To Kill a Mockingbird", "Harper Lee", "A classic of modern American literature", 12.99, "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg/330px-To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg"),
            Book(3, "Pride and Prejudice", "Jane Austen", "A romantic novel of manners", 8.99, "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/PrideAndPrejudiceTitlePage.jpg/330px-PrideAndPrejudiceTitlePage.jpg"),
            Book(4, "The Catcher in the Rye", "J.D. Salinger", "A novel about teenage angst and alienation", 11.99, "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/The_Catcher_in_the_Rye_%281951%2C_first_edition_cover%29.jpg/330px-The_Catcher_in_the_Rye_%281951%2C_first_edition_cover%29.jpg"),
            Book(5, "Moby-Dick", "Herman Melville", "The saga of Captain Ahab and his obsession with a white whale", 14.99, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Moby-Dick_FE_title_page.jpg/330px-Moby-Dick_FE_title_page.jpg"),
            Book(6, "The Lord of the Rings", "J.R.R. Tolkien", "An epic high-fantasy novel", 19.99, "https://upload.wikimedia.org/wikipedia/en/thumb/e/e9/First_Single_Volume_Edition_of_The_Lord_of_the_Rings.gif/330px-First_Single_Volume_Edition_of_The_Lord_of_the_Rings.gif"),
            Book(7, "The Hobbit", "J.R.R. Tolkien", "A fantasy novel and children's book", 9.99, "https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/TheHobbit_FirstEdition.jpg/330px-TheHobbit_FirstEdition.jpg"),
            Book(8, "Frankenstein", "Mary Shelley", "A Gothic novel and early example of science fiction", 7.99, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Frankenstein_1818_edition_title_page.jpg/330px-Frankenstein_1818_edition_title_page.jpg"),
            Book(9, "The Hunger Games", "Suzanne Collins", "A dystopian novel set in a post-apocalyptic world", 13.99, "https://upload.wikimedia.org/wikipedia/en/thumb/d/dc/The_Hunger_Games.jpg/330px-The_Hunger_Games.jpg"),
            Book(10, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "The first book in the Harry Potter series", 15.99, "https://upload.wikimedia.org/wikipedia/en/thumb/6/6b/Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg/330px-Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg"),
            Book(11, "The Da Vinci Code", "Dan Brown", "A mystery thriller novel", 12.99, "https://upload.wikimedia.org/wikipedia/en/thumb/6/6b/DaVinciCode.jpg/330px-DaVinciCode.jpg"),
            Book(12, "The Alchemist", "Paulo Coelho", "A philosophical novel", 10.99, "https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/TheAlchemist.jpg/330px-TheAlchemist.jpg"),
            Book(13, "The Girl with the Dragon Tattoo", "Stieg Larsson", "A psychological thriller novel", 14.99, "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Thegirlwiththedragontattoo.jpg/330px-Thegirlwiththedragontattoo.jpg"),
            Book(14, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "A comedy science fiction series", 11.99, "https://upload.wikimedia.org/wikipedia/en/thumb/b/bd/H2G2_UK_front_cover.jpg/330px-H2G2_UK_front_cover.jpg"),
            Book(15, "The Martian", "Andy Weir", "A science fiction novel about an astronaut stranded on Mars", 13.99, "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/The_Martian_2014.jpg/330px-The_Martian_2014.jpg"),
        ]

    def search(self, query):
        query = query.lower()
        return [book for book in self.books if query in book.title.lower() or query in book.author.lower()]

    def get_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None