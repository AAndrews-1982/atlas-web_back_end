#!/usr/bin/env python3
"""Personal data"""
import re
import logging
from typing import List
import os
import mysql.connector
from mysql.connector import connection


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """Obfuscate specified fields in a log message."""
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]+",
                         f"{field}={redaction}", message)
    return message

# Assuming filter_datum is defined elsewhere in your code
# from your_module import filter_datum


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Override the format method to filter and redact specific fields.

        Applies the filter_datum function to redact sensitive information
        from the log record's message before formatting it.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log message with sensitive data redacted."""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)

# Assuming RedactingFormatter is defined elsewhere in your code
# from your_module import RedactingFormatter

# Example PII fields - adjust these based on your user_data.csv


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """
    Creates a logger object named 'user_data'.
    The logger logs up to INFO level and does not propagate messages.
    It uses a StreamHandler with a RedactingFormatter.

    Returns:
        logging.Logger: Configured logger object.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create a StreamHandler with RedactingFormatter
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Establishes and returns a connection to the database.

    Uses environment variables for database credentials and host.
    Database name is obtained from PERSONAL_DATA_DB_NAME environment variable.

    Returns:
        MySQLConnection: Connection object to the MySQL database.
    """
    db_user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')  # Assumes env var is set

    try:
        return mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name
        )
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        raise
