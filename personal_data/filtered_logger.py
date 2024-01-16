#!/usr/bin/env python3
"""Filtered Logger Module

Provides functionality for filtering and obfuscating personal data in logs.
Includes `filter_datum` function and `RedactingFormatter` class for log message
redaction, ensuring sensitive information is not exposed in log outputs.

Functions:
    filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str
Classes:
    RedactingFormatter(logging.Formatter)
"""

import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector import connection

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.
    
    Args:
        fields: Fields to obfuscate.
        redaction: Replacement string for obfuscation.
        message: Original log message.
        separator: Delimiter separating fields in log message.

    Returns:
        Obfuscated log message.
    """
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]+", f"{field}={redaction}", message)
    return message

class RedactingFormatter(logging.Formatter):
    """
    A formatter class that redacts specified fields in log messages.
    
    Inherits from logging.Formatter, adding functionality to obfuscate
    specified personal data fields in log records.

    Attributes:
        REDACTION (str): Obfuscation replacement string.
        FORMAT (str): Log message format.
        SEPARATOR (str): Delimiter for fields in log message.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes RedactingFormatter with specified fields.
        
        Args:
            fields (List[str]): Fields to obfuscate in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record, obfuscating specified fields.
        
        Args:
            record (logging.LogRecord): Log record to format.

        Returns:
            Formatted and obfuscated log message.
        """
        return filter_datum(
            fields=self.fields,
            redaction=self.REDACTION,
            message=super().format(record),
            separator=self.SEPARATOR)

def get_logger() -> logging.Logger:
    """
    Creates and configures a logger object.

    Returns:
        Configured logger with redacting formatter.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Establishes and returns a database connection.

    Returns:
        Database connection object.
    """
    db_user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')
    try:
        return mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
