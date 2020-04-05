from papers.paper_product import PaperProduct


class Book(PaperProduct):
    def __init__(self, count_pages: int, price: float, title: str, author: str):
        super().__init__(count_pages, price, title)
        self.reviews = []
        self.author = author

    def change_title(self, new_title):
        if len(new_title) < 10:
            new_title = "Special Edition:" + new_title
        self.title = new_title
        print(f"Book {new_title} has edited its title.")

    def change_price(self, price):
        old_price = self.price
        new_price = price + 1.2
        self.price = new_price
        print(f"Price of the book is changed. It was {old_price}. New price is {new_price}.")

    def add_review(self, review, user):
        self.reviews.append((review, user))

    def reviews_count(self):
        return len(self.reviews)

    def __str__(self):
        result = f"The book '{self.title}' is written by {self.author} on {self.issue_date}\n"
        result += f"The following {self.reviews_count()} reviews are available:\n"
        for review in self.reviews:
            result += f"'{review[0]}' by {review[1]}"
        return result
