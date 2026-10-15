import unittest
from pathlib import Path

class FoodDeliveryTests(unittest.TestCase):
    def test_homepage_exists(self):
        self.assertTrue(Path("index.html").is_file())

    def test_menu_and_title(self):
        html = Path("index.html").read_text(encoding="utf-8")
        self.assertIn("FoodExpress", html)
        self.assertIn("Our Menu", html)

    def test_cart_functionality(self):
        html = Path("index.html").read_text(encoding="utf-8")
        self.assertIn("function addToCart", html)
        self.assertIn("Your Cart", html)

if __name__ == "__main__":
    unittest.main()
