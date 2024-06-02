### Fetch Products by Category

- **URL**: `/products/<category>`
- **Method**: GET
- **Parameters**:
  - `category` (string): The category of products to retrieve. Available categories: `leggings`, `accessories`.
- **Response**: JSON response containing product data for the specified category.

### Fetch All Products

- **URL**: `/products/all`
- **Method**: GET
- **Response**: JSON response containing product data for all categories.

### Caching

The application uses caching to improve performance and reduce the number of API requests made to the lululemon online store. Cached data is stored for a configurable period (default: 60 seconds) using Flask-Caching.

## App Documentation

### `app.py`

This file contains the main API code

2. **Helper Function**:
   - `fetch_product_data(url)`: Fetches and parses product data from a given URL.

3. **API Endpoints**:
   - `/products/<category>`: Retrieves product data for a specific category.
   - `/products/all`: Retrieves product data for all categories.

## Testing

To run the tests for this app:

```bash
pytest test_app.py
```