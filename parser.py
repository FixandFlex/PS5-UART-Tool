# parser.py

import re

def parse_uart_line(line):
    """
    Parses a raw UART line into (error_code, message, severity).
    Returns None if the format is invalid.
    
    Expected format (example):
    [E001] Fan Failure - CRITICAL
    [E002] Temp Sensor Degraded - MODERATE
    [E000] All Systems Normal - OK
    """
    pattern = r"\[(E\d{3})\]\s+(.+?)\s+-\s+(CRITICAL|MODERATE|OK)"
    match = re.match(pattern, line.strip(), re.IGNORECASE)
    
    if not match:
        return None

    error_code = match.group(1)
    message = match.group(2).strip()
    severity = match.group(3).lower()  # Normalize severity for DB

    return error_code, message, severity
