# CHROME TAB SPAMMER

A Python tool that opens as many Chrome tabs as you want. This script is designed for Windows only.

## Features

- Opens a specified number of Chrome tabs with a URL.
- Simple and easy to use.

## Requirements
- Python 3.x installed
- Google Chrome installed

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/chrome-tab-spammer.git
    cd chrome-tab-spammer
    ```

2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

## Usage

1. Open a command prompt or terminal.

2. Navigate to the directory where the script is located.

3. Run the script:

    ```sh
    python chrome_tab_spammer.py
    ```

4. Enter the number of tabs you would like to open when prompted.

## Code

```python
import subprocess

number = int(input("How Many Tabs Would You Like to Open: "))

def crash():
    processes = []
    for _ in range(number):
        processes.append(subprocess.Popen(["start", "chrome", "https://google.com"], shell=True))
    for process in processes:
        process.wait()

crash()
