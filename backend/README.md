# Stock Order Punching System - Backend

## Overview
The Stock Order Punching System is designed to manage and execute stock buy orders for multiple client accounts efficiently. It utilizes a global stock priority list to determine purchase orders while ensuring equal cash allocation per new stock and skipping stocks already held by clients.

## Features
- **Client Management**: Handles multiple client accounts with unique identifiers, cash balances, and stock holdings.
- **Global Priority Service**: Integrates a ranked list of stocks to prioritize purchases.
- **Order Execution**: Interfaces with a third-party API for placing buy orders.
- **Real-time Logging**: Provides a CLI logger for monitoring order processing and execution status.
- **Frontend Dashboard**: Offers a user-friendly interface for tracking execution status and logs.

## Setup Instructions
1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd stock-order-punching-system/backend
   ```

2. **Install Dependencies**
   Ensure you have Python 3.7+ installed. Then, install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Start the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

4. **Access the API**
   Open your browser and navigate to `http://localhost:8000/docs` to view the API documentation and test the endpoints.

## Usage
- **Trigger Order Processing**: Use the API endpoint to initiate order processing for clients.
- **Monitor Execution Status**: Check the frontend dashboard for real-time updates on order statuses and logs.

## Technologies Used
- **Backend**: Python, FastAPI, httpx, rich
- **Frontend**: React, Tailwind CSS
- **Logging**: Rich library for CLI logging

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.