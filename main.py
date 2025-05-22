# main.py

import os
from db import init_db
from gui import launch_gui  # Import launch_gui from gui.py

def create_directories():
    """Ensure required directories exist."""
    os.makedirs("logs", exist_ok=True)
    os.makedirs("data", exist_ok=True)

def main():
    print("🔧 Starting UART Diagnostic Tool...")
    
    # Step 1: Create required directories
    create_directories()

    # Step 2: Initialize SQLite database
    init_db()

    # Step 3: Launch the GUI
    launch_gui()  # Call the imported function

if __name__ == "__main__":
    main()
