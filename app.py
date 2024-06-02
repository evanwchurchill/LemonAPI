from flask import Flask, jsonify
from flask_caching import Cache
import requests

app = Flask(__name__)

# Configure Flask-Caching
app.config['CACHE_TYPE'] = 'simple'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Cache timeout in seconds

cache = Cache(app)

URLS = {
    'leggings': 'https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json',
    'accessories': 'https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json'
}

def fetch_product_data(url):
    """
    Fetches and parses product data from the given URL.

    Args:
        url (str): The URL to fetch product data from.

    Returns:
        list: A list of dictionaries representing product data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        products = list(map(lambda record: {
            "displayName": record['attributes']['product.displayName']
        }, data['contents'][0]['mainContent'][0]['contents'][0]['records']))
        return products
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error fetching or parsing data: {e}")
        return []

@app.route('/products/<category>', methods=['GET'])
@cache.cached(timeout=60)
def get_products(category):
    """
    Retrieves product data for the specified category.

    Args:
        category (str): The category of products to retrieve.

    Returns:
        Response: JSON response containing product data.
    """
    url = URLS.get(category)
    if not url:
        return jsonify({"error": "Invalid category"}), 400
    products = fetch_product_data(url)
    return jsonify(products)

@app.route('/products/all', methods=['GET'])
@cache.cached(timeout=60)
def get_all_products():
    """
    Retrieves product data for all categories.

    Returns:
        Response: JSON response containing product data for all categories.
    """
    all_products = []
    for category, url in URLS.items():
        products = fetch_product_data(url)
        all_products.extend(products)
    return jsonify(all_products)

if __name__ == '__main__':
    app.run(debug=True)
