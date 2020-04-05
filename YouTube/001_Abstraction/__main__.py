from papers import Book, Newspaper

book1 = Book(20, 20.5, "Fairy Tales", "J.K.J.")
book1.change_price(30)
book1.change_price(305)
book1.change_title("Funny Tales")
book1.add_review("A great and interesting book.", "Jo")
book1.add_review("Not that great.", "Joanna")
print(book1)

newspaper = Newspaper(30, 20, "Daily Sofia News", "daily")
print(newspaper.price)
newspaper.change_price(10)
print(newspaper.price)

book2 = Book(20, 20.5, "Tales", "J.K.J.")
book2.change_title("Fairy")
