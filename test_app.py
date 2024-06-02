import unittest
from app import app


class ProductAPITestCase(unittest.TestCase):
    """
    Test case for the product API endpoints.
    """

    def setUp(self):
        """
        Set up the test client and configure it for testing.
        """
        self.app = app.test_client()
        self.app.testing = True

    def test_get_products(self):
        """
        Test fetching products for different categories.
        """
        categories = ['leggings', 'accessories']

        for category in categories:
            with self.subTest(category=category):
                response = self.app.get(f'/products/{category}')
                self.assertEqual(response.status_code, 200)
                data = response.get_json()
                self.assertIsInstance(data, list)
                if data:
                    self.assertIn('displayName', data[0])

    def test_get_products_no_category(self):
        """
        Test accessing the products endpoint without specifying a category.
        """
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 404)  # Expecting 404 for missing route


if __name__ == '__main__':
    unittest.main()
