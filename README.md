# Hackathon Event Tracker

## Setup Instructions

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install dependencies using pip:
   ```sh
   pip install -r requirements.txt
   ```

## How it Works

The `tracker.py` script scrapes upcoming hackathon events from a specified URL and displays them in a formatted table. It also provides an option to save the results to a CSV file.

1. Run the script:
   ```sh
   python tracker.py
   ```
2. The script will fetch events from the default URL (`https://unstop.io/hackathons`). You can change this URL by modifying the `url` variable in the `main()` function.
3. The events will be displayed in a grid table format.
4. If you want to save the results, the script will prompt you to confirm.

## Dependencies

- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML content.
- `tabulate`: For displaying data in a formatted table.

These dependencies are listed in the `requirements.txt` file.
