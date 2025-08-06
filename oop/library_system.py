class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)    
        self.page_count = page_count


class Library():
    def __init__(self):
        self.books = [] # List to hold Book/Ebook/PrintBook instances

    def add_book(self, book):
        # Add a book to the library
        if isinstance(book, (Book, EBook, PrintBook)):
            self.books.append(book)
        else:
            raise TypeError
            
    def list_books(self):
        # Print details of all books in the library
        for book in self.books:
            if isinstance(book, EBook):
                print(f"Ebook: {book.title} by {book.author}, File Size : {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")

