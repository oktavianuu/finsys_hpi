# HPI Financial Management System

A financial management system designed for a small oil plantation named HPI. This system helps manage expenses, revenues, inventory, and payroll efficiently.

## Features

- **Expense Tracking**: Record and categorize all plantation expenses.
- **Revenue Management**: Track sales and manage invoices.
- **Inventory Management**: Monitor inventory levels and receive alerts for low stock.
- **Payroll Management**: Handle employee salaries and generate payslips.
- **Financial Reporting**: Generate income statements, balance sheets, and cash flow statements.
- **Analytics and Insights**: Use machine learning to predict expenses and provide financial insights.

## Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hpi-financial-system.git
   cd hpi-financial-system
2. Create and activate a virtual environment:
    ```bash 
    # On Windows
    python -m venv hpi_financial_system_env
    hpi_financial_system_env\Scripts\activate

    # On macOS/Linux
    python -m venv hpi_financial_system_env
    source hpi_financial_system_env/bin/activate
3. nstall the required packages:
    ```bash 
    pip install Flask SQLAlchemy pandas numpy scikit-learn

## Database Setup
1. Ensure the database is set up correctly by initializing it within the Flask application context. The tables will be created automatically when the application is first run.

## Running the Application
1. Start the flask application:
    ```bash 
    python app.py
2. The application will be available at ```http://localhost:5000```.

## API Endpoints
#### Expense Management
* Add Expense: 'POST /expenses'
    ```json
    {
    "category": "Maintenance",
    "amount": 150.00,
    "date": "2023-05-24"
    }
* Get Expenses: 'GET /expenses'
    ```json
    [
        {
            "category": "Maintenance",
            "amount": 150.00,
            "date": "2023-05-24"
        }
    ]
#### Revenue Management
* Add Revenue: POST /revenues
    ```json
    {
    "source": "Oil Sales",
    "amount": 1000.00,
    "date": "2023-05-24"
    }
* Get Revenues: GET /revenues
    ```json
    [
        {
            "source": "Oil Sales",
            "amount": 1000.00,
            "date": "2023-05-24"
        }
    ]
#### Inventory Management
* Add Inventory: POST /inventory
    ```json
    {
        "item_name": "Fertilizer",
        "quantity": 50,
        "last_updated": "2023-05-24"
    }
* Get Inventory: GET /inventory
    ```json
    [
        {
            "item_name": "Fertilizer",
            "quantity": 50,
            "last_updated": "2023-05-24"
        }
    ]
#### Payroll Management
* Add Payroll: POST /payroll
    ```json 
    {
        "employee_name": "John Doe",
        "salary": 2000.00,
        "pay_date": "2023-05-24"
    }
* Get Payroll: GET /payroll
    ```json
    [
        {
            "employee_name": "John Doe",
            "salary": 2000.00,
            "pay_date": "2023-05-24"
        }
    ]

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the LICENSE file for details. Feel free to customize the content, especially the URLs, and repository details according to your project's specifics.

