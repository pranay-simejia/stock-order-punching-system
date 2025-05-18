# CLI Logger for Stock Order Punching System

This directory contains the implementation of the CLI logger for the Stock Order Punching System. The logger is designed to provide real-time observability of the order processing system, allowing users to monitor stock processing, order statuses, and any errors that may occur during execution.

## Features

- Real-time logging of stock orders being processed.
- Display of order statuses, including successes and failures.
- Retry attempts and error logging for failed orders.
- Utilizes the `rich` library for enhanced CLI output.

## Installation

To use the CLI logger, ensure that the required dependencies are installed. You can install them using pip:

```
pip install rich
```

## Usage

To run the CLI logger, you can execute the `logger.py` script. This will start the logging process and display real-time updates in the terminal.

```bash
python logger.py
```

Make sure that the backend application is running to see the logs related to order processing.

## Contributing

Contributions to improve the CLI logger are welcome. Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.