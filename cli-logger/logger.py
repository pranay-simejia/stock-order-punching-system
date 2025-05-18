from rich.console import Console
from rich.table import Table
from rich.live import Live
import time

class Logger:
    def __init__(self):
        self.console = Console()
        self.table = Table(show_header=True, header_style="bold magenta")
        self.table.add_column("Client ID", style="dim")
        self.table.add_column("Stock", style="cyan")
        self.table.add_column("Quantity", style="green")
        self.table.add_column("Status", style="yellow")
        self.table.add_column("Message", style="white")

    def log_order(self, client_id, stock, quantity, status, message):
        self.table.add_row(client_id, stock, str(quantity), status, message)
        self.console.clear()
        with Live(self.table, refresh_per_second=10):
            time.sleep(1)

    def log_error(self, client_id, error_message):
        self.console.print(f"[red]Error for Client {client_id}: {error_message}[/red]")