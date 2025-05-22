# PS5DiagTool

PS5DiagTool is a lightweight Python-based diagnostic tool designed to interface with the PlayStation 5 motherboard via UART. It enables technicians to read, log, and manage error codes efficiently with a user-friendly graphical interface.

## Features

- Real-time UART communication with PS5 hardware
- Automatic parsing and logging of error codes with timestamps and severity levels
- Local SQLite database for error storage and management
- Export logged errors to CSV for easy reporting
- Reset and clear error logs functionality
- Simple and intuitive GUI for seamless user experience

## Installation

1. Download the latest installer from the [Releases][(https://github.com/FixandFlex/PS5-UART-Tool/releases/tag/v1.0.0) page.
2. Run the installer and follow the on-screen instructions.
3. By default, the application installs to your Desktop for easy access.

## Usage

1. Connect your PS5 motherboard to your PC via UART (e.g., USB-to-serial adapter).
2. Launch PS5DiagTool from the Desktop or Start Menu.
3. Select the correct COM port and baud rate (default is COM3, 9600 baud).
4. Start the UART listener to begin logging error codes.
5. Use the GUI options to export, reset, or clear logged data.

## Development

If you want to build or modify PS5DiagTool:

```bash
cd PS5DiagTool
pip install -r requirements.txt
python main.py
db.py
exporter.py
parser.py
uart_handler.py
