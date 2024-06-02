import unittest
from app import app, cache

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

    def test_get_products_leggings(self):
        """
        Test fetching products for the 'leggings' category.
        """
        category = 'leggings'
        response = self.app.get(f'/products/{category}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        if data:
            self.assertIn('displayName', data[0])

    def test_get_products_accessories(self):
        """
        Test fetching products for the 'accessories' category.
        """
        category = 'accessories'
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

    def test_caching(self):
        """
        Test caching behavior for product data retrieval.
        """
        category = 'leggings'
        
        # Clear cache
        with app.app_context():
            cache.clear()
        
        # First request should fetch fresh data
        response1 = self.app.get(f'/products/{category}')
        self.assertEqual(response1.status_code, 200)
        data1 = response1.get_json()
        
        # Second request should hit the cache
        response2 = self.app.get(f'/products/{category}')
        self.assertEqual(response2.status_code, 200)
        data2 = response2.get_json()

        # Data should be the same as it's coming from cache
        self.assertEqual(data1, data2)

        # Wait for the cache to expire
        time.sleep(61)
        
        # Third request should fetch fresh data again
        response3 = self.app.get(f'/products/{category}')
        self.assertEqual(response3.status_code, 200)
        data3 = response3.get_json()
        
        # Data should be the same, but it should be fetched freshly
        self.assertEqual(data1, data3)

if __name__ == '__main__':
    unittest.main()
