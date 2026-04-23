## Inventory Management System (Flask REST API + CLI)
Project Overview

This project is a Flask-based inventory management system designed for a retail environment. It provides a REST API for managing inventory items and a CLI tool for interacting with the API.

The system also integrates with the OpenFoodFacts external API to fetch real-world product data.


## Features
## REST API (Flask)

The API supports full CRUD operations:

Create inventory items
Retrieve all items
Retrieve a single item
Update items (PATCH)
Delete items
External API Integration


The CLI communicates with the Flask API using HTTP requests.

Testing

The project includes automated tests using pytest:

CRUD operations tested (create, read, update, delete)
External API tested using mocking
Flask test client used for API testing

Project Structure
inventory-system/

 app.py              # Flask REST API
cli.py              # Command-line interface
test_app.py        # Unit tests (pytest)
models.py          # Item structure (if used)
README.md          # Project documentation

## Installation

1. Clone repository
git clone 
cd inventory-system

2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install flask  requests pytest click

Running the Application
Start Flask server
python3 app.py

Server runs at:
http://127.0.0.1:5000

## CLI Usage
## List items
python cli.py list-items
Create item

python cli.py create --name Milk --barcode 123 --price 10 --quantity 5 --category dairy

## Get item
python cli.py get 1

## Update item
python cli.py update 1 --price 20

## Delete item
python cli.py delete 1

## Running Tests
pytest -v

## External API
This project uses:
OpenFoodFacts API
https://world.openfoodfacts.org/
Used to fetch real product data based on search terms.



## Development was done using feature branches:

main → stable production branch
feature/crud → CRUD implementation
feature/api → external API integration
feature/cli → CLI implementation
feature/tests → testing suite

Each feature was developed separately and merged into main.

## Author
Jeremy Njuguna
Flask Inventory Management System