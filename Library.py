class Library():
    
    def __init__(self):
        self.books = []

    def add_books(self, *args, log=False):
        for book in args:
            self.books.append(book)
            if log:
                print(f"Book named {book.title} added to library")

    def remove_books(self, *args, log=False):
        for book in args:
            if book in self.books:
                self.books.remove(book)
                if log:
                    print(f"Book named {book.title} removed from library")
        
    def show_books(self):
        print("\nBooks currently in the library :")
        for book in self.books:
            print(book)
    
    def borrow_book(self, person, title, then = None, catch = None):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                person.add_books(book)
                if then:
                    then()
                return
        if catch:
            catch()
                
    
    def return_book(self, person, title, then = None, catch = None):
        for book in person.books:
            if book.title.lower() == title.lower():
                person.books.remove(book)
                self.add_books(book)
                if then:
                    then()
                return
        if catch:
            catch()

    