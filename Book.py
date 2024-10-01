class Book():

    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.date = date
    
    def __str__(self) -> str:
        return f"{self.title} - {self.author} ({self.date})"