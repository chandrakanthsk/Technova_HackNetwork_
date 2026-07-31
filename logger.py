# logger.py

import logging


# Log file name
LOG_FILE = "network_monitor.log"


# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def log_info(message):
    """Record normal system activity."""

    logging.info(message)
    print(f"[INFO] {message}")


def log_warning(message):
    """Record warning events."""

    logging.warning(message)
    print(f"[WARNING] {message}")


def log_error(message):
    """Record errors."""

    logging.error(message)
    print(f"[ERROR] {message}")


def log_critical(message):
    """Record critical/high-risk events."""

    logging.critical(message)
    print(f"[CRITICAL] {message}")


# Test logger
if __name__ == "__main__":

    log_info("Network monitoring system started.")

    log_info("Connected to Core-Switch.")

    log_warning("New device detected: Laptop-10.")

    log_critical(
        "HIGH RISK: Unknown-Switch connected to Core-Switch Gi0/2."
    )

    log_error("Unable to connect to Switch-3.")