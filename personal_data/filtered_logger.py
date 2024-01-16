#!/usr/bin/env python3
"""Personal data"""
import re
import logging
from typing import List


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
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
