from rich.console import Console
from rich.logging import RichHandler
import logging

console = Console()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console)]
)

logger = logging.getLogger("stock_order_punching_system")

def log_order_processing(client_id, stock, quantity, status, message):
    if status == "success":
        logger.info(f"Order placed: Client {client_id} - Stock: {stock}, Quantity: {quantity} - {message}")
    else:
        logger.error(f"Order failed: Client {client_id} - Stock: {stock}, Quantity: {quantity} - {message}")

def log_retry_attempt(client_id, stock, attempt):
    logger.warning(f"Retry attempt {attempt} for Client {client_id} - Stock: {stock}")

def log_processing_status(client_id, status):
    logger.info(f"Processing status for Client {client_id}: {status}")