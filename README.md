# Student detail-
Name - Jai Nishant
USN -1MV21IS018


# Chocolate house ----->

# Description
lightweight web app to manage:
-  Seasonal flavors
-  Ingredient stock levels
-  Customer suggestions and allergy concerns

# Requirements
- Python 3.8+
- Flask framework
- SQLite

# Features
- Add/view seasonal chocolate flavors via APIs.
- Track stock levels of ingredients via APIs.
- Collect customer suggestions and allergy feedback via APIs.

# Setup
-  Clone this repository:
   ```bash
   git clone <unique_repo_url>
   ```
-  Enter the project directory:
   ```bash
   cd chocolate_shop
   ```
-  Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
-  Run the application:
   ```bash
   python app.py
   ```
-  Use a tool like Postman or Curl to interact with the API.

## API Endpoints
- `GET /` - Check API status.
- `GET /flavors` - List all flavors.
- `POST /flavors` - Add a new flavor (JSON body: `{"flavor_name": "string", "flavor_details": "string"}`).
- `GET /inventory` - List all stock items.
- `POST /inventory` - Add a new inventory item (JSON body: `{"ingredient_name": "string", "ingredient_quantity": int}`).
- `GET /feedback` - List all customer feedback.
- `POST /feedback` - Submit new feedback (JSON body: `{"customer_name": "string", "suggestion_text": "string", "allergy_details": "string"}`).

## Notes
- Inputs are validated to prevent invalid data.
- API is designed to return informative error messages on incorrect requests.