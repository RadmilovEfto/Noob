# virtualna biblioteka(def)
#Crud
# Dodaj Knigu
#izlistaj knigu
# Obrishi Knigu

print("DEL 1")


books = []


def add_book(book_name, book_author):
    books.append({"name": book_name, "author":book_author })
 # find book -> naci knigu po cenu?
print("DEL 3")


def find_book_by_name(name):
    for book in books :
        if book["name"]==name :
            return book


add_book("Harry Poter 1", "J.K. Rowling")
add_book("Harry Poter 2", "J.K. Rowling")

hp1 = find_book_by_name("Harry Poter 5")
if hp1 is None :
    print("Kniga ne postoi")
print(hp1)

#Brishenje kniga (po imenu)
# u slicaj da kniga ne postoi ispisati neku greshku

def delete_book_by_name(book_name):

    found_books = find_book_by_name(book_name)
    if found_books is None :
        print("Nema ta kniga")
    else :
        books.remove(found_books)
        print("Obrisana je Kniga")


delete_book_by_name("Harry Poter 1")
print(books)


