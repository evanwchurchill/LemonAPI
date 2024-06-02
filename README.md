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

## Code Documentation

### `app.py`

This file contains the main Flask application code. Here's an overview of the key components:

1. **Flask App Configuration**:
   - Configures Flask-Caching to cache API responses.
   - Defines the base URLs for different product categories.

2. **Helper Function**:
   - `fetch_product_data(url)`: Fetches and parses product data from a given URL.

3. **API Endpoints**:
   - `/products/<category>`: Retrieves product data for a specific category.
   - `/products/all`: Retrieves product data for all categories.

4. **Cache Configuration**:
   - Configures caching settings for API responses.

## Testing

Unit tests for the Flask app are included in the `tests/` directory. You can run the tests using the following command:

```bash
pytest tests/
```

## Contributing

Contributions to this Flask API project are welcome! Feel free to open issues or submit pull requests to improve the codebase.

## License

This Flask API project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
