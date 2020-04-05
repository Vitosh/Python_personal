from _datetime import datetime
from abc import ABC, abstractmethod


class PaperProduct(ABC):
    @abstractmethod
    def __init__(self, count_pages, price, title):
        self.count_pages = count_pages
        self.price = price
        self.title = title
        self.issue_date = datetime.now()

    @abstractmethod
    def change_title(self, new_title):
        raise NotImplementedError("Subclasses must override change_title()!")

    @abstractmethod
    def change_price(self, price):
        raise NotImplementedError("Subclasses must override change_price()!")