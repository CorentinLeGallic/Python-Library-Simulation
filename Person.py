class Person():
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.books = []
    
    def add_books(self, *books, log=False):
        for book in books:
            self.books.append(book)
            if log:
                print(f"Book named {book.title} added to {self.getName()}'s books")
    
    def remove_books(self, *books, log=False):
        for book in books:
            if book in self.books:
                self.books.remove(book)
                if log:
                    print(f"Book named {book.title} removed from {self.getName()}'s books")

    def show_books(self):
        print(f"\nBooks currently in {self.getName()}'s books :")
        for book in self.books:
            print(book)

    def getName(self):
        return f"{self.name.capitalize()} {self.surname.upper()}"
    
    def __str__(self) -> str:
        return f"{self.name.capitalize()} {self.surname.upper()}"