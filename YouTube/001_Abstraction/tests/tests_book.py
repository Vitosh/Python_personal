import unittest
from papers import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.my_book = Book(10, 20.0, "How to get 1K YouTube subscribers", "Joe")

    def tearDown(self):
        self.my_book = None
        print("tearDown() method has been called.")

    def test_init_book_and_check_author(self):
        actual = self.my_book.author
        expected = "Joe"
        self.assertEqual(expected, actual)
        # self.assertEqual(my_book.author, "Joe")

    def test_init_book_and_check_whether_reviews_are_empty_list(self):
        actual = self.my_book.reviews
        expected = []
        self.assertEqual(expected, actual)

    def test_change_price(self):
        self.my_book.change_price(100)
        actual = self.my_book.price
        expected = 101.2
        self.assertEqual(expected, actual)

    def test_change_title_small(self):
        self.my_book.change_title("VBA")
        actual = self.my_book.title
        expected = "Special Edition:VBA"
        self.assertEqual(expected, actual)

    def test_change_title_big(self):
        self.my_book.change_title("Some large title here")
        actual = self.my_book.title
        expected = "Some large title here"
        self.assertEqual(expected, actual)

    def test_whether_review_is_added(self):
        self.my_book.add_review("Great book", "Peter")
        actual = self.my_book.reviews[0][0]
        expected = "Great book"
        self.assertEqual(expected, actual)

    def test_whether_author_is_added(self):
        self.my_book.add_review("Great book", "Peter")
        self.my_book.add_review("Really great book", "Gosho")
        actual = self.my_book.reviews[1][1]
        expected = "Gosho"
        self.assertEqual(expected, actual)

    def test_review_count(self):
        self.my_book.add_review("Great book", "Peter")
        self.my_book.add_review("Really great book", "Gosho")
        self.my_book.add_review("Really great book", "Gosho")
        self.my_book.add_review("Really great book", "Gosho")
        self.my_book.add_review("Really great book", "Gosho")
        actual = self.my_book.reviews_count()
        expected = 5
        self.assertEqual(expected, actual)

    def test_adding_string_for_change_price(self):
        with self.assertRaises(TypeError) as cm:
            self.my_book.change_price("three fifty")
        self.assertEqual('can only concatenate str (not "float") to str', str(cm.exception))


if __name__ == "__main__":
    unittest.main()
