from papers.paper_product import PaperProduct


class Newspaper(PaperProduct):
    def __init__(self, count_pages: int, price: float, title: str, period: str):
        super().__init__(count_pages, price, title)
        self.period = period
        self.correctors = []

    def change_title(self, new_title):
        self.title = new_title
        print(f"Newspaper changed its title. New title is {self.title}.")

    def change_price(self, price):
        self.price = price * 0.9
        print(f"Newspaper now costs {self.price}.")