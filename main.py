from Library import *
from Book import *
from books import *
from Person import *

def main():
    biblio = Library()
    biblio.add_books(*books)

    personne = Person("Corentin", "Le Gallic")

    while True:
        try:
            action = int(input("\nWhat do you want to do ?\n[0 : Emprunter un livre] - [1 : Rendre un livre] - [2 : Afficher les livres de la bibliothèque] - [3 : Afficher les livres que vous possédez] "))
        
            if action == 0:
                book_title = input("Quel livre souhaitez-vous emprunter ? ")
                biblio.borrow_book(personne, book_title, lambda: print(f"Le livre {book_title} a été correctement emprunté !"), lambda: print(f"Impossible d'emprunter le livre {book_title}"))
            elif action == 1:
                book_title = input("Quel livre souhaitez-vous emprunter ? ")
                biblio.return_book(personne, book_title, lambda: print(f"Le livre {book_title} a été correctement rendu !"), lambda: print(f"Impossible de rendre le livre {book_title}"))
            elif action == 2 :
                biblio.show_books()
            elif action == 3:
                personne.show_books()
            else:
                raise ValueError

        except ValueError:
            print("Merci d'entrer un nombre entier compris entre 0 et 3")

if __name__=="__main__":
    main()