class Publication:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_info(self):
        return f"Title: {self.title}, Author: {self.author}"


class Book(Publication):
    _book_count = 0

    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.__isbn = isbn
        Book._book_count += 1

    @property
    def isbn(self):
        return self.isbn

    @isbn.setter
    def isbn(self, value):
        if not (isinstance(value, str) and len(value) == 13):
            raise ValueError("ISBN must be a 13-character string")
        self.__isbn = value

    def __str__(self):
        return f"Book: {self.title} by {self.author}, ISBN: {self.isbn}"

    def __eq__(self, other):
        return isinstance(other, Book)

    def __overdue__(self):
        return False

    @classmethod
    def get_book_count(cls):
        return cls._book_count


class EBook(Book):

    def __init__(self, title, author, isbn, file_format)
    super().__init__(self, title, author, isbn)
    self.file_format = file_format

    def show_info(self):
        super().show_info()
        print(f"File Format: {self.file_format}")


class Borrowable:

    def borrow(slef)
    print("Borrowing Item.")

    def return_item(slef)
    print("Returning Item.")


class Magazine(Publication, Borrowable):

    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def show_info(self):
        super().show_info()
        print(f"")
