class Book:

    def __init__(self, title, author, pub_year):
        self.title = title
        self.author = author
        self.pub_year = pub_year

    def __str__(self):
        return self.title


book = Book('Физика', 'Перышкин', 2013)

print(book)  # в выводе получим название книги
