#!/usr/bin/env python3
"""0. Regex-ing"""
import re


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
    fields: A list of strings representing all fields to obfuscate.
    redaction: A string representing by what the field will be obfuscated.
    message: A string representing the log line.
    separator: A string representing the character
    separating fields in the log line.

    Returns:
    A string with the specified fields obfuscated.
    """
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]+",
                         f"{field}={redaction}", message)
    return message
