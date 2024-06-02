import unittest
from app import app
from parameterized import parameterized


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
        self.FIELDS = ['displayName', 'defaultSKU', 'parentCategory']

    @parameterized.expand([
        ('leggings',),
        ('accessories',),
        ('all',),
    ])
    def test_get_products(self, category):
        """
        Test fetching products for categories, and all products.
        """
        endpoint = f'/products/{category}'
        response = self.app.get(endpoint)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        if data:
            for field in self.FIELDS:
                self.assertIn(field, data[0])

    def test_get_products_no_category(self):
        """
        Test accessing the products endpoint without specifying a category.
        """
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 404)  # Expecting 404 for missing route


if __name__ == '__main__':
    unittest.main()
