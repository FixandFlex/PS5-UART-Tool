import serial
from datetime import datetime
from parser import parse_uart_line
from db import insert_error
import time

def start_uart_listener(port='COM3', baudrate=9600):
    """
    Start reading UART data from the specified port.
    Automatically parses and logs messages.
    """
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"📡 Listening on {port} at {baudrate} baud...")

        while True:
            try:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    print(f"> {line}")
                    parsed = parse_uart_line(line)
                    if parsed:
                        timestamp = datetime.now().isoformat()
                        error_code, message, severity = parsed
                        insert_error(timestamp, error_code, message, severity)
                    else:
                        print("⚠️ Could not parse line.")
                time.sleep(0.1)
            except UnicodeDecodeError:
                print("⚠️ Unicode decode error, skipping line.")
            except Exception as e:
                print(f"⚠️ Error reading UART line: {e}")

    except serial.SerialException as e:
        print(f"❌ Serial error: {e}")
    except KeyboardInterrupt:
        print("🛑 UART listener stopped.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
