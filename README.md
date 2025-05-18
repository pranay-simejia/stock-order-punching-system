# Stock Order Punching System

## Overview
The Stock Order Punching System is a high-performance application designed to manage buy orders for multiple client accounts. It utilizes a global stock priority list to determine purchase orders while ensuring equal cash allocation per new stock. The system is built to minimize turnaround time (TAT) for API firing and provides real-time observability through a CLI logger and a frontend dashboard.

## Objectives
- Manage buy orders for multiple client accounts.
- Use a global stock priority list to decide purchase orders.
- Ensure equal cash allocation per new stock.
- Skip stocks already held by a client.
- Minimize TAT for API firing.

## Architecture
The project is structured into three main components:

1. **Backend**: 
   - Built with FastAPI, it handles order processing, execution, and logging.
   - Contains modules for API endpoints, order processing logic, and data models.

2. **Frontend**: 
   - Developed using React and Tailwind CSS, it provides a user interface for monitoring execution status and logs.
   - Communicates with the backend via API calls.

3. **CLI Logger**: 
   - Implements real-time logging of stock processing and order statuses using the rich library.

## Technologies
- **Backend**: Python, FastAPI, asyncio, httpx, rich
- **Frontend**: JavaScript/TypeScript, React, Tailwind CSS
- **CLI Logger**: Python, rich

## Setup Instructions
### Backend
1. Navigate to the `backend` directory.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend
1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

### CLI Logger
1. Navigate to the `cli-logger` directory.
2. Run the logger:
   ```
   python logger.py
   ```

## Usage
- Clients can place buy orders through the frontend dashboard.
- The backend processes orders based on the global priority list and client holdings.
- Real-time logs and execution status are available in the frontend and CLI logger.

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.